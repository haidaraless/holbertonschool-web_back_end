#!/usr/bin/env python3
"""
Complex annotations - iterable object
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """annotate function's parameters and return values
    with appropraite types"""

    return [(i, len(i)) for i in lst]
