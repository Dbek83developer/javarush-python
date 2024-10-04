# Извлечение информации из исключения

# Напишите функцию read_integer, которая принимает строку и пытается преобразовать её в целое число.
# Если возникает ValueError, обработайте исключение и выведите аргументы ошибки и тип ошибки.
# Дополнительно, сохраните исключение в переменной и выведите её за пределами блока except.

# Напишите тут ваш код
def read_integer(txt):
    error = ""
    try:
        result = int(txt)
    except ValueError as e:
        error = e
        print(f"Произошла ошибка: {e}")
        print(f"Аргументы ошибки: {e.args}")
        # print(f"Сообщение об ошибке: {str(e)}")
    finally:
        print(error)


read_integer("dfdff")
read_integer(44)