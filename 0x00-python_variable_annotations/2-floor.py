#!/usr/bin/env python3
"""Write a type-annotated function floor that takes a
float n as argument and returns the floor of the float
"""

import math


def floor(n: float) -> int:
    """Function takes a float n and returns
    the floor of the float
    Args:
        n (float): n
    Returns:
        int : a floored float
    """
    return math.floor(n)
