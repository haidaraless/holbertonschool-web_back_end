#!/usr/bin/env python3
"""
Complex annotations - list of mixed floats and integers
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function accepts a list of mixed float and int numbers
    and returns sum of them"""
    return float(sum(mxd_lst))
