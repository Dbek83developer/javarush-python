# Создание файла

# Напишите программу, которая создает новый файл example.txt и записывает в него строку "This is a new file."

# Напишите тут ваш код
file = open('example.txt', 'w')
file.write("This is a new file.\n")
file.close()