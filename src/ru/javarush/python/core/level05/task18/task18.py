# Чистим список
import random
# Напишите программу, которая создает список из 10 случайных чисел в диапазоне от 1 до 20.
# Затем программа должна удалить из списка все четные числа с использованием цикла.
# Программа должна вывести исходный и обновленный списки.

# Напишите тут ваш код
alist = [random.randint(1, 20) for _ in range(10)]
print(alist)
blist = []
for item in range(len(alist)-1, -1, -1):
    if alist[item] % 2 == 0:
        del alist[item]
    else:
        blist.append(alist[item])
# blist = [x for x in alist if x % 2 != 0]
print(alist)
