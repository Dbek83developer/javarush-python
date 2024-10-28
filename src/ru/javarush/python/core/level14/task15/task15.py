# Асинхронный контекстный менеджер
import asyncio
# Напишите асинхронный контекстный менеджер, который будет печатать сообщения при входе и выходе из контекста.
# Внутри контекста выполните асинхронную задержку на 2 секунды и выведите сообщение "Внутри контекста".


class AsyncContextManager:
    async def __aenter__(self):
        print("Enter context")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("Exit context")


async def main():
    async with AsyncContextManager():
        await asyncio.sleep(2)
        print("Inside context")

asyncio.run(main())
