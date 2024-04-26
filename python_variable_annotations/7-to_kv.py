#!/usr/bin/env python3
"""to_kv"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a tuple from a string and the square of a number
"""
    return (k, v**2)
