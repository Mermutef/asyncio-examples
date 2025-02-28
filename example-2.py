import asyncio
import nest_asyncio
import time

start = time.time()


def tic():
    return f"({time.time() - start:.2f} c)"


async def task(name, delay):
    print(f"Задача {name} запущена {tic()}")
    await asyncio.sleep(delay)
    print(f"Задача {name} выполнена {tic()}")
    return f"Результат задачи {name} {tic()}"


async def main_1():
    tasks = [
        task("А", 2),
        task("Б", 1),
        task("В", 3)
    ]
    # запускаем все задачи, ждем их завершения и собираем все результаты
    results = await asyncio.gather(*tasks)
    # Коррутины будут перенесены в будущее и запланированы в цикле обработки событий.
    # Они не обязательно будут запланированы в том же порядке, в котором они были переданы.
    # Все коррутины должны совместно использовать один и тот же цикл обработки событий.
    # Если все задачи выполнены успешно, результатом возвращаемой коррутины будет список результатов
    # (в порядке исходной последовательности, не обязательно в порядке поступления результатов).
    print("\nВсе задачи выполнены")
    print("\n".join(results))


if __name__ == "__main__":
    nest_asyncio.apply()  # Разрешаем потоки внутри потока
    asyncio.run(main_1())
    end_time = time.time()
    print(f"\nВремя исполнения программы: {end_time - start:.2f} секунд")
