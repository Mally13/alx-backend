#!/usr/bin/env python3
"""
Contains a function named index_range that takes two integer arguments
page and page_size
"""


def index_range(page, page_size):
    """
    Returns a tuple of size two containing start index and
    end index corresponding to the range of indexes to return
    in a list for those particular pagination parameters
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
