#!/usr/bin/env python3
"""Simple helper function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """index_range function"""
    startIndex = (page - 1) * page_size
    endIndex = page * page_size
    return (startIndex, endIndex)
