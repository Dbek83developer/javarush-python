# Итерация по строкам файла

# Напишите программу, которая читает файл example.txt построчно, используя итератор, и выводит каждую строку на экран.

file = open('example.txt', 'r')

for line in file:
    print(line.strip())

file.close()
