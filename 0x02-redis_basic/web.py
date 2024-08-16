#!/usr/bin/env python3

import redis
import requests
from functools import wraps

r = redis.Redis()


def url_access_count(method):
    """Decorator to enhance get_page with caching and access counting."""
    @wraps(method)
    def wrapper(url):
        """Cache results and count URL accesses."""
        # Increment the count each time a URL is accessed
        key_count = "count:" + url
        current_count = r.incr(key_count)

        # Check if the URL is already cached
        key = "cached:" + url
        cached_value = r.get(key)
        if cached_value:
            # If cached, return the cached value
            return cached_value.decode("utf-8")
        else:
            # If not cached, fetch the content and cache it
            html_content = method(url)
            r.set(key, html_content, ex=10)
            return html_content
        return wrapper


@url_access_count
def get_page(url: str) -> str:
    """Fetch and return the HTML content of a specified URL."""
    results = requests.get(url)
    return results.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
