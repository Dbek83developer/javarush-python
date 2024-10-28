# Обработка исключений Future
import asyncio
# Напишите программу, которая создает объект Future и устанавливает для него исключение через 2 секунды.
# Используйте метод set_exception для установки исключения и обработайте это исключение после его возникновения.


async def set_exp(fut, delay):
    await asyncio.sleep(delay)
    fut.set_exception(ValueError("value error"))


async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    await asyncio.create_task(set_exp(fut, 2))
    try:
        result = await fut
    except ValueError as e:
        print(f"Caught od exception {e}")

asyncio.run(main())
