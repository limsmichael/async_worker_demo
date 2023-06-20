import asyncio
import random
from typing import Optional


class Producer:
    def __init__(self, limit: int = 1000):
        self.total = 0
        self.limit = limit

    async def put_work(self, queue: asyncio.Queue):
        while self.total < self.limit:
            # do some work
            value = (random.randint(1, 100) ** random.randint(1, 10))/random.randint(1, 10)
            # put the value into the queue
            await queue.put((value, self.total))
            self.total += 1

    async def run(self, queue: asyncio.Queue):
        await self.put_work(queue)
        await asyncio.sleep(0.1)
