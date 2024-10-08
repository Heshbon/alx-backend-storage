#!/usr/bin/env python3
""" Defines a Cache class for interacting with Redis, handling storage
and retrieval of data."""


import redis
import uuid
import functools
from typing import Union, Optional, Callable, Any


def count_calls(method: Callable) -> Callable:
    """ Decorator to count method calls in Redis. """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """ Increment call count and call the original method. """
        key = f"count:{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator to log inputs and outputs of a function. """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        key = method.__qualname__
        self._redis.rpush(f"{key}:inputs", str(args).encode())
        result = method(self, *args, **kwargs)
        self._redis.rpush(f"{key}:outputs", result)
        return result
    return wrapper


class Cache:
    """ Cache class to store and retrieve data in Redis. """

    def __init__(self, host='localhost', port=6379, db=0):
        """ Initialize Redis client and clear existing data. """
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in Redis with a unique key. """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Any]] = None
            ) -> Optional[Union[str, bytes, int, float]]:
        """ Retrieve data from Redis and optionally convert it. """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data.decode('utf-8')

    def get_count(self, key: str) -> Optional[int]:
        """ Retrieve an integer count from Redis. """
        value = self._redis.get(key)
        if value is None:
            return None
        return int(value)

    def get_str(self, key: str) -> Optional[str]:
        """ Retrieve a string from Redis. """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """ Retrieve an integer from Redis. """
        value = self.get(key)
        if value is None:
            return None
        try:
            return int(value)
        except ValueError:
            return None

    def replay(self, method: Callable):
        """ Display history of calls for a method. """
        method_name = method.__qualname__
        inputs_key = f"{method_name}:inputs"
        outputs_key = f"{method_name}:outputs"

        inputs = self._redis.lrange(inputs_key, 0, -1)
        outputs = self._redis.lrange(outputs_key, 0, -1)

        print(f"{method_name} was called {len(inputs)} times:")
        for input_str, output_str in zip(inputs, outputs):
            input_decode = input_str.decode('utf-8')
            output_decode = output_str.decode('utf-8')
            print(f"{method_name} {input_decode} -> {output_decode}")
