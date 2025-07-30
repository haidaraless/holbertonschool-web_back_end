#!/usr/bin/env python3

"""Basics of async functions"""

import asyncio
import random


async def wait_random(max_delay: int = 10):
    """wait for random seconds and return delay time"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
