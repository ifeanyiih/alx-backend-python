#!/usr/bin/env python3
"""Write a type-annotated function to_kv that takes a string
k and an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k. The second element is the
square of the int/float v and should be annotated as a float
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function takes a string and an int or float as argument
    and returns a tuple
    Args:
        k (str): k
        v (int | float): v
    Returns:
        tuple: a tuple of a str and a float
    """
    return (k, v**2)
