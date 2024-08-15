#!/usr/bin/env python3
""" A get_page function to fetch HTML content of URLs with caching
"""

import redis
import requests
from functools import wraps

# Initialize Redis client
r = redis.Redis()


def url_access_count(method):
    """Decorator to enhance get_page with caching."""
    @wraps(method)
    def wrapper(url):
        """Cache results and count URL access."""
        # Increment the count
        key_count = "count:" + url
        r.incr(key_count)

        # Check if the URL is cached
        key = "cache:" + url
        cached_value = r.get(key)
        if cached_value:
            # If cached, return cached value
            return cached_value.decode("utf-8")
        else:
            # If not cached, fetch the content and cache it
            html_content = method(url)
            r.set(key, html_content, ex=10)
            return html_content
    return wrapper


@url_access_count
def get_page(url: str) -> str:
    """Fetch and return the HTML content"""
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    content = get_page('http://slowwly.robertomurray.co.uk')
    print(content)
