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

    def store(self, data: Union[str, bytes, float, int]) -> str:
        """Generate a random key and store data in the cache."""
        key = str(uuid.uuid4())
        if isinstance(data, (str, bytes, int, float)):
            self._redis.set(key, data)
        return key
    def get(self, key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, float, int, None]:
        """Retrieve data from the cache."""
        res = self._redis.get(key)
        if res is None:
            return None
        if fn is not None:
            return fn(res)
        return res

    def get_str(self, key: str) -> Optional[str]:
        """Get string from the cache."""
        res = self.get(key, fn=str)
        return res

    def get_in(self, key: str) -> Optional[int]:
        """Get integers from the cache."""
        res = self.get(key, fn=int)
        return res
