# Группировка кортежей

# Напишите программу, которая создает кортеж из 6 элементов, запрашиваемых у пользователя.
# Затем программа должна сгруппировать их в 3 картежа по 2 элемента.
# Затем объединить 1 и 3 кортежи и вывести обновленный кортеж на экран.

# Напишите тут ваш код
alist = [input("Enter: ") for _ in range(6)]
my_tuple = tuple(alist)
sub_tuple1 = my_tuple[:2]
sub_tuple2 = my_tuple[2:4]
sub_tuple3 = my_tuple[4:]
new_tuple = (sub_tuple1 + sub_tuple3)
# print(sub_tuple3)
print(new_tuple)
