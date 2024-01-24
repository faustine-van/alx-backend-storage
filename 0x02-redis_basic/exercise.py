#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Optional
from typing import Callable


class Cache():
    """cache"""
    def __init__(self, flushdb=False):
        self._redis = redis.Redis()
        if flushdb:
            self._redis.flushdb()

    def store(self, data: Union[str, float, int, bytes]) -> str:
        """generate a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable[[bytes], Union[str, float, int]]] = None
            ) -> Optional[Union[str, float, int]]:
        """generate a random key"""
        res = self._redis.get(key)
        if res is None:
            return None
        if fn is not None:
            return fn(res)
        return res

    def get_str(self, key: str) -> str:
        """get string"""
        res = self.get(key, fn=lambda x:  x.decode())
        return res

    def get_in(self, key: str) -> str:
        """get integers"""
        res = self.get(key, fn=lambda x: int(x.decode()))
        return res
