# Словарь.

# Напишите программу, которая создает словарь с информацией о человеке (например, имя, возраст и город) тремя различными способами:
# Использование фигурных скобок {}.
# Использование функции dict() с последовательностью пар ключ-значение.
# Использование функции dict() с именованными аргументами.
# Программа должна вывести все три словаря.

# Напишите тут ваш код
slovar1 = {"name":"Alex", "age": 20, "city": "Guangzhou"}
print(slovar1)
person = dict([("name", "John"), ("age", 30), ("city", "New York")])
print(person)
person2 = dict(name="John", age=30, city="New York")
print(person2)