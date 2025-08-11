#!/usr/bin/env python3

"""Module: pagination helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """returns a tuple with start, end indexes for pagination"""

    start: int = (page - 1) * page_size
    end: int = start + page_size
    return tuple([start, end])
