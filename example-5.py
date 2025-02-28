import time
import asyncio

start = time.time()


def tic():
    return f"({time.time() - start:.2f} c)"


async def fn():
    print(f"Один {tic()}")
    await asyncio.sleep(1)
    # await fn2()
    # просто так убрать await мы не можем, иначе поток зациклится и начнет вызывать сам себя
    # для запуска коррутины fn2() оборачиваем ее как задачу и запускаем
    # при этом, fn2() будет выполняться только в те моменты, когда не будет выполняться fn()
    asyncio.create_task(fn2())
    print(f'Четыре {tic()}')
    await asyncio.sleep(1)  # попробуй поменять тут время и посмотри что будет меняться в выводе и как
    print(f'Пять {tic()}')
    await asyncio.sleep(1)


async def fn2():
    # await asyncio.sleep(1)
    print(f"Два {tic()}")
    await asyncio.sleep(1)  # попробуй поменять тут время и посмотри что будет меняться в выводе и как
    print(f"Три {tic()}")


asyncio.run(fn())
