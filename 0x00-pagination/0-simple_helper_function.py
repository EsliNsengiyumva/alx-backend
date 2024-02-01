#!/usr/bin/env python3
"""Pagination helper function.
"""
def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate start and end index for pagination.

    Args:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple: Start and end index for the specified pagination parameters.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1

    return start_index, end_index
