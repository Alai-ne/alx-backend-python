#!/usr/bin/env python3

python
import asyncio
import random

async def wait_random(max_delay: float = 10.0) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds and return the delay.

    Args:
        max_delay (float, optional): The maximum delay in seconds. Defaults to 10.0.

    Returns:
        float: The random delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
