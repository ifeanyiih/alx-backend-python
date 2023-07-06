#!/usr/bin/env python3
"""Write a type-annotated function sum_list
which takes a list input_list of floats as
argument and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a list of floats and Returns the sum
    Args:
        input_list (list[float]): input_list
    Returns:
        float: sum of list items
    """
    sum_of_list: float = 0.0
    for n in input_list:
        sum_of_list = sum_of_list + n
    return sum_of_list
