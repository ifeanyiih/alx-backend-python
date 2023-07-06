#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier that takes a
float multiplier as argument and returns a function that multiplies
a float by a multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function returns a function that multiplies a
    float by a multiplier
    Args:
        multiplier (float): multiplier
    Returns:
        function: a function that multiples a float by a multiplier
    """
    def multiply(x: float) -> float:
        """multiples x by multiplier and returns the value
        Args:
            x (float): x
        Returns:
            float: x * multiplier
        """
        return x * multiplier
    return multiply
