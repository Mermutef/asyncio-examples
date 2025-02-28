import time
import asyncio

start = time.time()


def tic():
    return f"({time.time() - start:.2f} c)"


async def fn():
    print(f"Зашли в fn {tic()}")
    print(f"Один {tic()}")
    await asyncio.sleep(1)  # благодаря await fn() ждем, пока пройдет 1 секунда
    # если убрать await, то код просто пойдет исполняться дальше (см. example-5.py)
    await fn2()  # ждем пока выполнится коррутина fn2()
    print(f'Четыре {tic()}')
    await asyncio.sleep(1)
    print(f'Пять {tic()}')
    await asyncio.sleep(1)


async def fn2():
    print(f"Зашли в fn2 {tic()}")
    await asyncio.sleep(1)
    print(f"Два {tic()}")
    await asyncio.sleep(1)
    print(f"Три {tic()}")


asyncio.run(fn())
