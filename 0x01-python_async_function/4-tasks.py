#!/usr/bin/env python3
""" Task 4 """
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Task 4 """
    new_list = []
    for ind in range(n):
        new_list.append(task_wait_random(max_delay))
    return sorted(new_list)
