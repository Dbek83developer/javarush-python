# В глубинах самых глубин.

# Напишите программу, которая создает словарь с информацией о человеке (например, имя, возраст, адрес, и контактная информация).
# Программа должна:
# Изменить значения верхнего уровня, вложенного словаря и более глубокого уровня вложенности.
# Добавить новый элемент в вложенный словарь.
# Удалить элемент из вложенного словаря и верхнего уровня.

# Напишите тут ваш код
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "address": {
        "street": "123 Main St",
        "zip": "10001"
    },
    "contact": {
        "phone": "1233-345-998",
        "email": "dbek.developer@gmail.com"
                }
}


def print_dict(d, indent=0):
    for index, (key, value) in enumerate(d.items()):
        if index == 0:
            d[key] = "None"
        # if index == 1:
        #     d.pop(key)
        print("  " * indent + str(key) + ": ", end="")
        if isinstance(value, dict):
            print()
            print_dict(value, indent + 1)
        else:
            print(value)


print_dict(person)
print(person)
