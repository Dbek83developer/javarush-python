# Ищем ключи.

# Напишите программу, которая создает словарь с информацией о книге (например, название, автор, год издания). Программа должна:
# Вывести все ключи словаря с использованием метода keys().
# Итерировать по всем ключам и вывести их на экран.

# Напишите тут ваш код
slv = {"title": "Garri Poter", "author": "Mike", "year": 2000}
for key in slv.keys():
    print(key)