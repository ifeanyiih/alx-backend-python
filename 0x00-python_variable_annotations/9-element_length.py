#!/usr/bin/env python3
"""Annotate functions parameters and return values
with the appropriate types
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """duck typing an iterable object"""
    return [(i, len(i)) for i in lst]
