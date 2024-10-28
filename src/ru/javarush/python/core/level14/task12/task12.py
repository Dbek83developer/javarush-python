# Отмена задачи

# Напишите асинхронную программу, которая создает задачу, выполняющую ожидание 5 секунд.
# Запустите её, подождите 1 секунду, затем отмените задачу и выведите сообщение о её отмене.
# Обработайте исключение CancelledError.

import asyncio

async def main():
    task = asyncio.create_task(asyncio.sleep(5))
    await asyncio.sleep(1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Task was cancelled")

asyncio.run(main())