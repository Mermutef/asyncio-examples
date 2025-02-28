import time
import asyncio

start = time.time()


def tic():
    return f"({time.time() - start:.2f} c)"


async def gr1():
    # Busy waits for a second, but we don't want to stick around...
    print(f'gr1 начала работу {tic()}')
    await asyncio.sleep(2)
    print(f'gr1 закончила работу {tic()}')


async def gr2():
    # Busy waits for a second, but we don't want to stick around...
    print(f'gr2 начала работу {tic()}')
    await asyncio.sleep(2)
    print(f'gr1 закончила работу {tic()}')


async def gr3():
    # пока gr1 и gr2 заблокированы (await asyncio.sleep(2))
    # коррутина gr3 может занимать все процессорное время для выполнения
    print(f"Делаем что-то, пока коррутины заблокированы {tic()}")
    await asyncio.sleep(1)
    print(f"Сделали! {tic()}")


if __name__ == "__main__":
    ioloop = asyncio.new_event_loop()
    asyncio.set_event_loop(ioloop)
    tasks = [
        ioloop.create_task(gr1()),
        ioloop.create_task(gr2()),
        ioloop.create_task(gr3())
    ]
    ioloop.run_until_complete(asyncio.wait(tasks))
    ioloop.close()
