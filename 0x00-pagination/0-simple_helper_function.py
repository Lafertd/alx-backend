#!/usr/bin/env python3
"""
module that contain a simple helper function
"""
def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end indices for the items in a given page

    Args:
        page (int): The 1-indexed number of the page
        page_size (int): The number of items in a page

    Returns:
        tuple: A tuple containing the start and the end of the index range

    """
    end = page * page_size
    start = end - page_size
    return (start, end)
