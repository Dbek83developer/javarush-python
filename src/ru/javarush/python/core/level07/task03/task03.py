# Проверка на пустоту.

# Напишите программу, которая создает несколько словарей с различным количеством элементов.
# Программа должна:
# Вывести количество элементов в каждом словаре.
# Проверить, пустой ли каждый словарь, и вывести соответствующее сообщение.
# Для проверки пустоты словаря нужно создать функцию check_empty

# Напишите тут ваш код
def check_empty(slv):
    if not slv:
        print("Dict is empty")
    else:
        print("Dict is not empty")


slv1 = {1: "sd", 2: "ks"}
slv2 = {1: "sd", 2: "ks", "dd": "dsfsdfsd"}
slv3 = {1: "sd", 2: "ks", 5: "sd", 6: "ks"}
print(len(slv1), len(slv2), len(slv3))
check_empty(slv1)
check_empty(slv2)
check_empty(slv3)

