# Четкий список
import random
# Напишите программу, которая создает список из 10 целых чисел.
# С использованием цикла for замените все четные элементы списка на строку "четное".
# Программа должна вывести обновленный список.

# Напишите тут ваш код
chetkiy = []
for _ in range(10):
    chetkiy.append(random.randint(0,100))

for (index, item) in enumerate(chetkiy):
    if item % 2 == 0:
        chetkiy[index] = "четное"
print(chetkiy)
