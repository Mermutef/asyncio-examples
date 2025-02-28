import time
import asyncio

start = time.time()


def tic():
    return f"({time.time() - start:.2f} c)"


async def fn():
    print(f'Это {tic()}')
    await asyncio.sleep(1)
    print(f'асинхронное программирование {tic()}')
    await asyncio.sleep(1)
    print(f'но не мультипоточное {tic()}')


asyncio.run(fn())
