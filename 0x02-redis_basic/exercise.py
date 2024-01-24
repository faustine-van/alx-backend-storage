#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """Cache class"""

    def __init__(self, flushdb: bool = False):
        self._redis = redis.Redis()
        if flushdb:
            self._redis.flushdb()

    def store(self, data: Union[str, float, int]) -> str:
        """Generate a random key and store data in the cache."""
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable[[bytes], Union[str, float, int]]] = None
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
        res = self.get(key, fn=lambda x: x.decode())
        return res

    def get_in(self, key: str) -> Optional[int]:
        """Get integers from the cache."""
        res = self.get(key, fn=lambda x: int(x.decode()))
        return res
