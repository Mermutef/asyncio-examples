import time
import asyncio

start = time.time()


def tic():
    return f"({time.time() - start:.2f} c)"


async def foo():
    print(f'Работает foo {tic()}')  # что-то делаем
    await asyncio.sleep(0)  # с помощью await передаем управление снова в поток событий, а сами пока ждем
    print(f'Снова работает в foo но дальше {tic()}')  # продолжаем делать с того места, где остановились


async def bar():
    print(f'Работает в bar {tic()}')  # что-то делаем
    await asyncio.sleep(0)  # передаем управление в поток событий ioloop, пока до нас нова очередь не дойдет
    print(f'Снова работает в bar, но дальше {tic()}')  # продолжаем с того момента, где остановились


if __name__ == "__main__":
    ioloop = asyncio.new_event_loop()  # создаем новый пустой поток событий
    asyncio.set_event_loop(ioloop)  # устанавливаем его как рабочий в данный момент
    tasks = [ioloop.create_task(foo()), ioloop.create_task(bar())]  # создаем задачи
    # задачи можно создавать либо в коррутинах (async def), либо с помощью create_task
    # сами задачи могут быть только коррутинами
    wait_tasks = asyncio.wait(tasks)  # собираем все задачки в одну кучку (список ожидания запуска)
    ioloop.run_until_complete(wait_tasks)  # запускаем, пока все не закончатся
    ioloop.close()  # закрываем поток
