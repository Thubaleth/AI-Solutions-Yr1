import asyncio
import aiohttp
import time

async def fetch(session,url):
    async with session.get(url) as response:
        print(f"Fetched {url} Status: {response.status}")
        return await response.text()

async def main():
    urls = [
       "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
        "https://httpbin.org/delay/1",
        "https://python.org",

    ]

    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session,url) for url in urls]
        results = await asyncio.gather(*tasks)

    print(f"\nTotal time: {time.time() - start:.2f} seconds")
    print(f"Fetched {len(results)} pages")

asyncio.run(main())

