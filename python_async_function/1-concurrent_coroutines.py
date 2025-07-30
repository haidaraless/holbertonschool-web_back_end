#!/usr/bin/env python3

"""execute multiple coroutines at the same time"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times"""
    delays = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(delays)
