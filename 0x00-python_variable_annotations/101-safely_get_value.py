#!/usr/bin/env python3
"""module to write annotation to function"""
from typing import Union, Any, Mapping, TypeVar

T = TypeVar('T', int, float)


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """function to use TypeVar and return according"""
    if key in dct:
        return dct[key]
    else:
        return default
