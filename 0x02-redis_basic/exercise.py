#!/usr/bin/env python3
""" Defines a Cache class for Redis with methods to store
and retrieve data.
"""

import redis
import uuid
import functools
from typing import Union, Optional, Callable, Any


def count_calls(method: Callable) -> Callable:
    """ Count the number of calls to a function.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """ The increment call count and execute the method
        """
        key = f"count:{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """ Handles data in Redis with unique keys.

    Arguments:
        _redis (redis.Redis): The redis client instance.
    """

    def __init__(self, host='localhost', port=6379, db=0):
        """ Initialize Redis client and clear the database
        """
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in Redis with a unique key.

        Arguments:
            data: The data to store (str, bytes, int, or float).

        Returns:
            The unique key for the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[callable] = None
            ) -> Union[str, bytes, int, float]:
        """ Retrieves and optionally convert data from Redis by key.

        Arguments:
            key: The key for the data.
            fn: The optional function to convert the data.

        Returns:
            The retrieved data, converted if fn is provided,
            or None if key doesn't exist.
        """
        data = self._redis.get(key)
        if data is None:
            return data
        if fn:
            callable_fn = fn(data)
            return callable_fn
        else:
            return data

    def get_str(self, key: str) -> str:
        """ Retrieves a string from Redis.

        Arguments:
            key: The key for the data.

        Returns:
            Retrieved string or None if the key doesn't exist.
        """
        value = self._redis.get(key, fn=lambda x: x.decode('utf-8'))
        return value

    def get_int(self, key: str) -> int:
        """ Retrieve an integer from Redis.

        Arguments:
            key: The key for the data.

        Returns:
            Retrieved integer or None if the key doesn't exist
            or conversion fails.
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            return None

        return value

    def replay(method: Callable):
        """ Print the call history of a method.
        """
        instance = method.__self__
        method_name = method.__qualname__
        inputs_key = f"{method_name}:inputs"
        outputs_key = f"{method_name}:outputs"

        inputs = instance._redis.lrange(inputs_key, 0, -1)
        outputs = instance._redis.lrange(outputs_key, 0, -1)

        print(f"{method_name} was called {len(inputs)} times:")
        for input_str, output_str in zip(inputs, outputs):
            input_decode = input_str.decode('utf-8')
            output_decode = output_str.decode('utf-8')
            print(f"{method_name} {input_decode} -> {output_decoded}")
