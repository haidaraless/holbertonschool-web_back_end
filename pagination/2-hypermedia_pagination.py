#!/usr/bin/env python3
"""Module: Hypermedia pagination data"""

import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """paginate data"""

        assert isinstance(page, int) and page > 0, 'must > than 0'
        assert isinstance(page_size, int) and page_size > 0, 'must > than 0'

        data = self.dataset()

        start, end = index_range(page, page_size)

        if start >= len(data):
            return list()

        return list(data[start:end])
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict():
        data_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(data_page),
            "page": page,
            "data": data_page,
            "next_page": (page + 1) if page < total_pages else None,
            "prev_page": (page - 1) if page > 1 else None,
            "total_pages": total_pages
        }
