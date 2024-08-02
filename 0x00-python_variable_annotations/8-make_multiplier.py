#!/usr/bin/env python3
"""module to return function that multiplies float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function to return function which multiply
       float by mulitiplier(float)
    """
    def multiplier_function(val: float) -> float:
        """multiply value by multiplier"""
        return val * multiplier
    return multiplier_function
