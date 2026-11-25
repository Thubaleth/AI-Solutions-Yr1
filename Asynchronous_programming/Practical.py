"""Write a program that:

1. Creates 5 asynchronous tasks
2. Each task prints its number, waits for 1–3 seconds randomly, then prints ‘done’
3. All tasks should run concurrently
4. Print total execution time

"""


import asyncio
import time
import random

async def task(number):
    delay = random.randint(1, 3)
    print(f"Task {number} started. waiting {delay} seconds.....")

    await asyncio.sleep(delay)
    print(f"Task {number} done")

async def main():
    start = time.time()

    async with asyncio.TaskGroup() as tg:
        for number in range(1,6):
            tg.create_task(task(number))


asyncio.run(main())
