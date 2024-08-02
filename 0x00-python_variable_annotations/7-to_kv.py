#!/usr/bin/env python3
"""module to return tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple of string and float or integer"""
    return (k, v*v)
