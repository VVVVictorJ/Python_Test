import asyncio
import time


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        # factorial("A", 2),
        # factorial("B", 3),
        # factorial("C", 4),
        say_after(1, '1'),
        say_after(2, '2'),
        say_after(3, '3')        
    )
    print(L)

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
