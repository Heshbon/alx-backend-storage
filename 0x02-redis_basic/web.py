#!/usr/bin/env python3
""" Script to fetch and cache web page content with Redis."""

import redis
import requests
from functools import wraps
from urllib.parse import quote

# Initialize Redis client
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)


def url_access_count(method):
    """ Decorator to cache page content and count accesses."""
    @wraps(method)
    def wrapper(url):
        """ Cache result and track URL access count."""
        encoded_url = quote(url)  # Encode URL to use as Redis key
        key_count = f"count:{encoded_url}"
        r.incr(key_count)  # Increment the count each time a URL is accessed

        key_cache = f"cached:{encoded_url}"
        cached_value = r.get(key_cache)
        if cached_value:
            # If cached, return the cached value
            return cached_value
        else:
            # Fetch and cache the content if not cached
            try:
                html_content = method(url)
                r.setex(key_cache, 10, html_content)  # Cache for 10 seconds
                return html_content
            except requests.RequestException as e:
                # Return error message if request fails
                return f"Error fetching URL: {e}"
    return wrapper


@url_access_count
def get_page(url: str) -> str:
    """ Fetch and return HTML content of a URL."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.text


if __name__ == "__main__":
    # Test the function
    url = 'http://slowwly.robertomurray.co.uk'
    print(get_page(url))
