# Использование оператора with для работы с файлами

# Напишите программу, которая открывает файл example.txt в режиме добавления, записывает в него строку "Новая линия.".
# Нужно корректно обрабатывать исключение FileNotFoundError, закрывая файл в любом случае.
# Нужно использовать оператор with для автоматического закрытия файла.

try:
    with open('example.txt', 'a') as file:
        file.write("Новая линия.\n")
        # file.write("This is a test file.\n")
        raise Exception("Something went wrong")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Caught an exception: {e}")


