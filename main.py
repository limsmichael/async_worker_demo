import asyncio
import time
from producer import Producer
from consumer import Consumer


async def main():
    start = time.time()

    # define the number of workers
    n_workers = 100
    # create a queue to pass data between producer/consumer
    queue = asyncio.Queue()

    # create the producer instance
    producer = Producer(limit=10000)
    # create a task from the run method
    producer_task = asyncio.create_task(producer.run(queue))
    # allow the task to prime the queue
    await asyncio.sleep(0.1)

    # create n_workers number of consumers
    consumers = [Consumer() for _ in range(n_workers)]
    # create the tasks for the workers
    workers = [asyncio.create_task(consumer.run(queue)) for consumer in consumers]

    # wait for the queue to be empty (hit the work limit)
    await queue.join()

    # cancel the tasks
    producer_task.cancel()
    for worker in workers:
        worker.cancel()
    print(f'total elapsed: {time.time() - start}')


if __name__ == "__main__":
    asyncio.run(main())
