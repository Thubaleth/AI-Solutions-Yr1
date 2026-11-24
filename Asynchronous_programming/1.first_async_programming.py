import asyncio
import time

async def task(name,delay):
    print(f"Starting{name}")
    await asyncio.sleep(delay)  # Non-blocking sleep
    print(f"Finished{name}")

async def main():
    start = time.time()

    #Runs tasks concurrently
    await asyncio.gather(
        task("A",2),
        task("B",3),
        task("C",1)
    )

    print(f"Total time: {time.time() - start:.2F} seconds")

asyncio.run(main())



