#!/usr/bin/env python3
"""Hypermedia pagination"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple:
    """index_range function"""
    startIndex = (page - 1) * page_size
    endIndex = page * page_size
    return (startIndex, endIndex)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_page function"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        startIndex, endIndex = index_range(page, page_size)
        if startIndex is None or endIndex is None:
            return []
        return self.dataset()[startIndex:endIndex]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """get_hyper function"""

        data = self.get_page(page, page_size)
        totalPages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page+1 if page < totalPages else None,
            "prev_page": page-1 if page > 1 else None,
            "total_pages": totalPages,
        }
