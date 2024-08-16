#!/usr/bin/env python3
""" Script to fetch and cache web page content with Redis."""

import redis
import requests
from functools import wraps
from urllib.parse import quote

# Initialize Redis client
try:
    r = redis.Redis()
    # Test Redis connection
    r.ping()
except redis.ConnectionError as e:
    print(f"Redis connection error: {e}")
    exit(1)


def sanitize_url(url):
    """ Encode URL to handle special characters in Redis keys. """
    return quote(url, safe='')


def url_access_count(method):
    """ Decorator to cache page content and count accesses."""
    @wraps(method)
    def wrapper(url):
        """ Cache result and track URL access count."""
        sanitized_url = sanitize_url(url)
        key_count = f"count:{sanitized_url}"
        key_cache = f"cached:{sanitized_url}"

        # Increment access count
        r.incr(key_count)

        # Check if cached content exists
        cached_value = r.get(key_cache)
        if cached_value:
            # Return cached content
            return cached_value.decode("utf-8")
        else:
            # Fetch and cache content if not cached
            try:
                html_content = method(url)
                r.set(key_cache, html_content, ex=10)  # Cache for 10 seconds
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
    url = 'http://slowwly.robertomurray.co.uk'
    print(get_page(url))
