#!/usr/bin/env python3
""" Task 8 """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Task 8 """
    def f(x: float) -> float:
        """ Task 8 """
        return multiplier * x
    return f
