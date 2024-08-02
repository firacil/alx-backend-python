#!/usr/bin/env python3
"""module to augment the following with
   correct duck-typed annotations
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """function returning lst according"""
    if lst:
        return lst[0]
    else:
        return None
