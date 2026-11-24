import asyncio

async def say_hello(name):
     print(f"Hello,{name}")
     await asyncio.sleep(1)
     print(f"Goodbye, {name}!")

async def main():
     # Method 1: await one by one (sequential)
     await say_hello("Alice")
     await say_hello("Bob")

     print("----------Concurrent-------------------")

     #Method 2:concurrent
     await asyncio.gather(
        say_hello("Charlie"),
        say_hello("Diana")
     )

asyncio.run(main())
     