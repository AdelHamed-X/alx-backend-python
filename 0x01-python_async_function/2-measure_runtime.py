#!/usr/bin/env python3
""" Task 2 """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, delay_max: int) -> float:
    """ Task 2 """
    start = time.time()

    asyncio.run(wait_n(n, delay_max))

    end = time.time()
    elapsed_time = end - start

    return elapsed_time / n
