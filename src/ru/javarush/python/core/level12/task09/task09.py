# Чтение бинарного файла

# Напишите программу, которая читает бинарный файл example.bin и выводит его содержимое в консоль в виде байтов.

file = open('example.bin', 'rb')
content = file.read()
print(content)
file.close()