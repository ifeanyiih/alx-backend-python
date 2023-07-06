#!/usr/bin/env python3
"""Write a type-annotated function sum_mixed_list which
takes a list mxd_lst of integers and floats and returns their sum
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Function sums the content of a mixed list
    Args:
        mxd_list (list): mxd_list
    Returns:
        float: the sum of the list contents
    """
    sums: float = 0
    for n in mxd_lst:
        sums = sums + n
    return sums
