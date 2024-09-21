# Лес

# Напишите программу, которая создает список из названий деревьев, затем с использованием цикла и функции enumerate() выводит каждый элемент списка и его индекс.

# Напишите тут ваш код
trees = ["oak", "apple", "chinor", "leap"]
for (index, value) in enumerate(trees):
    print(value, index)