# Объединение и пересечение

# Напишите программу, которая создает два множества из элементов, запрашиваемых у пользователя.
# Программа должна объединить эти множества с использованием метода union() и найти их пересечение с использованием метода intersection().
# Программа должна вывести оба результата

# Напишите тут ваш код
first = set([input("enter: ") for _ in range(3)])
second = set([input("enter: ") for _ in range(3)])
union = first.union(second)
print(union)
print(first.intersection(second))
