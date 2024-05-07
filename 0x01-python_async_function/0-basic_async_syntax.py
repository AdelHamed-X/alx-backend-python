#!/usr/bin/env python3
""" Task 0 """
import asyncio
import random


async def wait_random(int: max_delay=10) -> float:
    """ Task 0 """
    random_int = random.uniform(0, max_delay)
    test = await asyncio.sleep(random_int)
    return random_int
