#!/usr/bin/env python3
"""module to appropratly annotate below functions"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function to return types and annotation"""
    return [(i, len(i)) for i in lst]
