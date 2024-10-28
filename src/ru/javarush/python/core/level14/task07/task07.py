# Управление задачами (Tasks)

# Напишите асинхронную программу, которая создает две задачи.
# Первая задача должна ждать 1 секунду и печатать "Первая задача завершена",
# вторая задача должна ждать 2 секунды и печатать "Вторая задача завершена".
# Используйте asyncio.create_task() для создания задач и asyncio.run() для их выполнения.
import asyncio


async def say_hello(msg, delay):
    await asyncio.sleep(delay)
    print(msg)


async def main():
    task1 = asyncio.create_task(say_hello('Первая задача завершена', 1))
    task2 = asyncio.create_task(say_hello('Вторая задача завершена', 2))
    await task1
    await task2

asyncio.run(main())
