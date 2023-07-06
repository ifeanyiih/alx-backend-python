#!/usr/bin/env python3
"""Write a type-annotated function sum_mixed_list which
takes a list mxd_lst of integers and floats and returns
their sum as a float.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """Takes a mixed list of floats and ints and
    Returns the sum as float
    Args:
        mxd_lst (list[float | int]): mxd_lst
    Returns:
        float: sum of list items
    """
    sum_of_list: float = 0.0
    for n in mxd_lst:
        sum_of_list = sum_of_list + n
    return sum_of_list
