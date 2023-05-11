import asyncio


async def nested():
    return 42


async def main():
    # nested()
    print(await nested())  # will print "42".


asyncio.run(main())
