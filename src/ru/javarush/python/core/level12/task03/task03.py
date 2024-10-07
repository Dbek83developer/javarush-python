# Чтение всего файла

# Напишите программу, которая читает и выводит на экран содержимое файла example.txt полностью.

file = open('example.txt', 'r')
txt = file.read()
print(txt)
file.close()