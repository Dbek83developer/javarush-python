# Использование объекта Future
import asyncio
# Напишите программу, которая создает объект Future и устанавливает для него результат через 3 секунды.
# Используйте метод set_result для установки результата и выведите результат объекта Future после его завершения.


async def set_future_result(fut, delay):
    await asyncio.sleep(delay)
    fut.set_result("future is come")


async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    asyncio.create_task(set_future_result(fut, 3))
    result = await fut
    print(result)

asyncio.run(main())
