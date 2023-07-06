#!/usr/bin/env python3
"""Augmenting code with the correct duck-typed annotations"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Augment function with the correct
    duck-typed annotations
    """
    if lst:
        return lst[0]
    else:
        return None
