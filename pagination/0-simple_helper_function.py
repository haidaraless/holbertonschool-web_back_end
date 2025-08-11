#!/usr/bin/env python3
def index_range(page: int, page_size: int):
    start: int = (page - 1) * page_size
    end: int = start + page_size
    return tuple([start, end])
