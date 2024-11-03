#!/usr/bin/env python3
import csv
import math
from typing import List


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
    start = page_size * (page - 1)
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset

        Returns:
        List[List]: The dataset except the header row
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page from the dataset

        Args:
        page (int): The 1-indexed number of the page
        page_size (int): The number of items in a page

        Returns:
        List[List]: A list of rows corresponding to the requested page
        """

        data_object = Server.dataset(self)
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        interval = index_range(page, page_size)
        if interval[0] >= len(data_object) or interval[0] < 0:
            return []

        result = [row for row in data_object[interval[0]: interval[1]]]
        return result

    def get_hyper(self, page: int, page_size: int) -> dict:
        """
        Create a dictionary of key:value pairs

        Args:
        page_size (int):
        page (int):

        Returns:
        dict{}: dictionary containing the page_size, page, data, next_page, prev_page, total_pages

        """
        page_data = self.get_page(page, page_size) # list[list] of get_page()
        start, end = index_range(page, page_size) # tuple(start, end)

        data = page_data
        page_size = len(data)
        next_page = page + 1
        prev_page = page - 1
        total_pages = math.ceil(len(self.dataset()) / page_size) if page_size > 0 else 0

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page if next_page <= total_pages else None,
            "prev_page": prev_page if prev_page > 0 else None,
            "total_pages": total_pages
        }
