#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """Cache class"""

    def __init__(self):
        """declare"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, float, int]) -> str:
        """Generate a random key and store data in the cache."""
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
