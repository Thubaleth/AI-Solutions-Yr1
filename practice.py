import asyncio

async def fetch_data(delay):
    print("Fetching data.....")
    await asyncio.sleep(delay)
    print("data fetched")
    return{"data":"some data"} 


#define another coroutine that calls the first routine
async def main():
    print("Start of main coroutine")
    task = fetch_data(4)
    #await the fetch_data coroutine,pausing execution of main until fetch_data completes
    result = await task
    print(f"Recived result: {result}")
    print("End of main coroutine")

#Run the main coroutine
asyncio.run(main())
    

