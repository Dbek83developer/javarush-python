# Замена

# Напишите программу, которая создает множество, содержащее названия нескольких фруктов.
# Программа должна вывести фрукты на экран.
# Затем программа должна запросить у пользователя индекс (с учетом порядка вывода на экран) и новое название фрукта для замены.
# Затем найти фрукт по индексу, заменить его новым названием и вывести обновленное множество.
# Напишите тут ваш код
try:
    fruits = {"apple", "banana", "grape"}
    print(fruits)
    index = int(input("index: "))
    value = input("new fruit: ")
    alist = list(fruits)
    alist[index] = value
    fruits = set(alist)
    # fruits.update(index, value)
    print(fruits)
except IndexError:
    print("Index error")
