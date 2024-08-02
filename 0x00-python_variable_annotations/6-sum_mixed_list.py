#!/usr/bin/env python3
"""module to return sum of list mixed type of int and float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ function to return sum of list as a float"""
    return sum(mxd_lst)
