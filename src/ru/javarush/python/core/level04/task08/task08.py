import math
# Сравнивать очень просто
# python
eps = 1e-6
# Напишите программу, которая запрашивает у пользователя два вещественных числа и сравнивает их с использованием допустимой погрешности epsilon.
# Выведите результат сравнения на экран.

# Напишите тут ваш код
number1 = float(input("Enter the number: "))
number2 = float(input("Enter the number: "))
isEqual = abs(number1 - number2) < eps
print(isEqual)