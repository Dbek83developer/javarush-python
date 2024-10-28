# Запуск и остановка цикла событий

# Напишите программу, которая запускает цикл событий в бесконечном режиме.
# Запланируйте остановку цикла через 3 секунды, используя метод call_later.
# Публикация состояния запущен ли цикл до и после вызова метода stop().
import asyncio


def my_callback(loop):
    print(loop.is_running())
    loop.stop()


loop = asyncio.new_event_loop()
loop.call_later(3, my_callback, loop)
loop.run_forever()
