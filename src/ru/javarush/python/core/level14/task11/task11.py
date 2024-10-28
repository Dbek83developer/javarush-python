# Управление циклом событий

# Напишите асинхронную программу, которая создает две задачи.
# Первая задача должна печатать "Первая задача" и ждать 2 секунды,
# вторая задача должна печатать "Вторая задача" и ждать 3 секунды.
# Используйте asyncio.create_task() для создания задач и выполните их параллельно, дождавшись завершения обеих.
import asyncio


async def say_hello(msg, delay):
    print(msg)
    await asyncio.sleep(delay)


async def main():
    task1 = asyncio.create_task(say_hello('Первая задача', 2))
    task2 = asyncio.create_task(say_hello('Вторая задача', 3))
    await task1
    await task2

asyncio.run(main())