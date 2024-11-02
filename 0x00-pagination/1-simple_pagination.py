import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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
    return start, end


class Server:
    DATA_FILE = "data.csv"

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
        """
        Get a page from the dataset
        """
        data_object = self.dataset()
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)

        result = [row for row in data_object[start:end]]
        return result
