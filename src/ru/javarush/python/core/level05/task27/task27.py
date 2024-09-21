# Сумма кортежей

# Напишите программу, которая создает кортеж, содержащий несколько вложенных кортежей из целых чисел.
# Программа должна использовать цикл for для вычисления суммы всех элементов во вложенных кортежах и вывести результат.

# Напишите тут ваш код
my_tuple = ((1, 2, 3), (8, 9), (11, 2, 4, 5))
total = 0
for inner_tuple in my_tuple:
    for number in inner_tuple:
        total += number
#     total += number
# for number in my_tuple[3:5]:
#     total += number
# for number in my_tuple[5:]:
#     total += number

print(f"Сумма элементов кортежа: {total}")
