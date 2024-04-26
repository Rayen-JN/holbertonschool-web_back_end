#!/usr/bin/env python3
"""make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a function that multiplies a float by a multiplier
"""

    def multiply_func(n: float) -> float:
        return n * multiplier

    return multiply_func
