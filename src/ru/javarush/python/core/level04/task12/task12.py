# Неизвестность

# Напишите программу, которая запрашивает у пользователя два числа.
# Если пользователь не вводит значение (пустая строка), используйте значение по умолчанию None для этого числа.
# Вычислите и выведите сумму этих чисел.

# Напишите тут ваш код
num1 = input("Enter the number: ")
num2 = input("Enter the number: ")
if num1 == "":
    num1 = None
if num2 == "":
    num2 = None
if num1 is None or num2 is None:
    print("Сумма чисел неизвестна")
else:
    summa = int(num1) + int(num2)
    print(summa)