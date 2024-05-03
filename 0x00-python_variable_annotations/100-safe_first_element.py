#!/usr/bin/env python3
""" Task 10 """
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Task 10 """
    if lst:
        return lst[0]
    else:
        return None
