#!/usr/bin/env python3
"""Script to fetch and cache web page content with Redis."""

import redis
import requests
from functools import wraps

# Initialize Redis client
r = redis.Redis()


def url_access_count(method):
    """Decorator to cache page content and count accesses."""
    @wraps(method)
    def wrapper(url):
        """Cache result and track URL access count."""
        key_count = f"count:{url}"
        r.incr(key_count)  # Increment access count

        key_cache = f"cached:{url}"
        cached_value = r.get(key_cache)
        if cached_value:
            # Return cached value if available
            return cached_value.decode("utf-8")
        else:
            # Fetch and cache the content if not cached
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
    """Fetch and return HTML content of a URL."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.text
