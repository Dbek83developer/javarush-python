# Асинхронный генератор
import asyncio
# Напишите асинхронный генератор, который будет генерировать числа от 0 до 2 с задержкой в 1 секунду между числами.
# Используйте этот генератор в асинхронной функции, чтобы вывести значения на экран.


async def async_generator():
    for i in range(3):
        await asyncio.sleep(1)  # Асинхронная задержка
        yield i  # Генерация значения


async def main():
    async for value in async_generator():
        print(value)

asyncio.run(main())
