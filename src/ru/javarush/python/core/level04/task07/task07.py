import math
# Круглый математик

# Напишите программу, которая запрашивает у пользователя вещественное число и округляет его вниз (с использованием math.floor()),
# вверх (с использованием math.ceil()) и до ближайшего целого числа (с использованием round()).
# Выведите результаты всех трех округлений.

# Напишите тут ваш код
number = float(input("ENter float number: "))
print(math.floor(number), math.ceil(number), round(number))
