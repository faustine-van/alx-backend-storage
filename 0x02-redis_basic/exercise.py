#!/usr/bin/env python3
"""Writing strings to Redis"""
from functools import wraps
import redis
import uuid
from typing import Union, Optional, Callable


def count_calls(method: Callable) -> Callable:
    """ Increment the call count"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        # Increment the count in Redis
        count = self._redis.incr(key)
        # Call the original method
        result = method(self, *args, **kwargs)
        print(count)
        return result
    return wrapper


class Cache:
    """Cache class"""

    def __init__(self):
        """declare"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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

    def get_int(self, key: str) -> Optional[int]:
        """Get integers from the cache."""
        res = self.get(key, fn=int)
        return res
