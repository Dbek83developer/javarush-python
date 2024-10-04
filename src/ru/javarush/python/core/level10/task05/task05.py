# Обработка исключений.

# Напишите функцию safe_division, которая принимает два числа и выполняет их деление.
# Обработайте исключения, которые могут возникнуть при делении на ноль
# и при передаче некорректных значений (например, строки вместо чисел).
# Функция должна возвращать сообщение об ошибке или результат деления.

# Напишите тут ваш код
def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error is ZeroDivisionError"
    except TypeError:
        return "Error is TypeError"


print(safe_division(3, 5))
print(safe_division(4, 0))
print("wew", 'hkhjk')
