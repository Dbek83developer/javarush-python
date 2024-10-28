# Метод sleep()
import asyncio
# Напишите асинхронную функцию, которая принимает строку и задержку в секундах, затем выводит строку после указанной задержки.
# Создайте две задачи, каждая из которых вызывает эту функцию с разными строками и задержками.
# Запустите их одновременно, используя метод asyncio.run().


async def slp_prt(text, delay):
    await asyncio.sleep(delay)
    print(text)


async def main():
    task1 = asyncio.create_task(slp_prt('Salom', 3))
    task2 = asyncio.create_task(slp_prt('Nihao', 2))
    await asyncio.gather(task1, task2)

asyncio.run(main())
