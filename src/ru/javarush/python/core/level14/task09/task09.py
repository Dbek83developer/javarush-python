# Создание и получение цикла событий

# Напишите программу, которая создает новый цикл событий, устанавливает его как текущий и печатает его.
# Затем создайте еще один новый цикл событий и снова установите его как текущий.
# Убедитесь, что вы правильно меняете циклы событий.
import asyncio

new_loop1 = asyncio.new_event_loop()
asyncio.set_event_loop(new_loop1)
print(asyncio.get_event_loop())  # Текущий цикл событий
new_loop2 = asyncio.new_event_loop()
asyncio.set_event_loop(new_loop2)
print(asyncio.get_event_loop())
