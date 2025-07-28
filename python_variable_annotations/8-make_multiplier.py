#!/usr/bin/env python3
"""
Complex annotations - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function accepts a float number
    and returns a callable function that multiplies a float"""

    def multiply(n: float) -> float:
        return n * multiplier

    return multiply
