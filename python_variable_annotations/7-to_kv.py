#!/usr/bin/env python3
"""
Complex annotations - string and int, float to tuple
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function accepts a string and float or int number
    and returns a tuple of string and float"""
    return tuple([k, v**2])
