#!/usr/bin/env python3
""" Task 1 """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Task 1 """
    new_list = []
    for ind in range(n):
        new_list.append(await wait_random(max_delay))
    return sorted(new_list)
