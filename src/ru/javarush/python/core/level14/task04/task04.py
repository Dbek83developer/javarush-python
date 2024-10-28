# Выполнение нескольких задач параллельно

# Напишите программу, которая использует asyncio.gather() для выполнения нескольких асинхронных задач параллельно
# и собирает их результаты.

import asyncio

# Определение корутины, которая будет выполнена с задержкой
async def say_after(delay, what):
    # Приостанавливаем выполнение на заданное время
    await asyncio.sleep(delay)
    print(what)

# Основная корутина
async def main():
    # Создаем задачи для параллельного выполнения корутин
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    # Ждем завершения обеих задач
    res = await asyncio.gather(task1, task2)
    # await task1
    # await task2
    # print(res)

# Запуск основной корутины
asyncio.run(main())
