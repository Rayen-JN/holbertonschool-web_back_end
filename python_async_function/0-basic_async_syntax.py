#!/usr/bin/env python3

"""
An asynchronous coroutine that waits for a random delay
between 0 and max_delay seconds.
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    ''' Wait up to max_delay seconds and then return length of delay. '''
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
