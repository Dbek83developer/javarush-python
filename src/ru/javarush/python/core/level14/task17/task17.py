# Асинхронный итератор

# Напишите асинхронный итератор, который будет возвращать числа от 1 до 5 с задержкой в 1 секунду между числами.
# Используйте этот итератор в асинхронной функции, чтобы вывести числа на экран.

import asyncio

class AsyncIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current > self.end:
            raise StopAsyncIteration

        await asyncio.sleep(1)  # Имитация асинхронной задержки
        self.current += 1
        return self.current

async def main():
    async for number in AsyncIterator(0, 4):
        print(number)

asyncio.run(main())