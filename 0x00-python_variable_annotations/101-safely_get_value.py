#!/usr/bin/env python3
"""More involved type annotations. Adding the correct
anotations to function. If it looks like a Duck
"""
from typing import Union, Any, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Given the parameters and the return values,
    add type annotations to the function
    Args:
        dct (dictionary): dct
        key: (unknown): key
        default: (specified | None): default
    Returns:
        dictionary item or None
    """
    if key in dct:
        return dct[key]
    else:
        return default
