# Обработка ошибок при работе с файлами

# Напишите программу, которая открывает файл example.txt в режиме добавления, записывает в него строку "Новая линия.".
# Нужно корректно обрабатывать исключение FileNotFoundError, закрывая файл в любом случае.

try:
    file = open('example.txt', 'a')
    file.writelines("Новая линия.")
except FileNotFoundError:
    print("File not found")
    # file.close()
finally:
    file.close()
