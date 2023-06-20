import asyncio
import random


class Consumer:
    def __init__(self):
        self.total = 0

    async def run(self, queue: asyncio.Queue):
        while True:
            try:
                await self.process_work(queue)
            except asyncio.CancelledError:
                return

    async def process_work(self, queue: asyncio.Queue):
        # get work from the queue
        value, idx = await queue.get()
        try:
            # process the work from the queue
            processed = value / random.randint(1, 100)
            # simulate more work with sleep (allows hand off)
            await asyncio.sleep(0.1)
            print(processed, idx)
        except Exception as e:
            # catch all for errors
            print(e)
            pass
        # mark the work as done
        queue.task_done()
        self.total += 1
