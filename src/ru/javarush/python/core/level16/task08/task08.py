# Хеш-функция для словаря

# Напиши свою хеш-функцию, которая возвращает целое число от 0 до 10к для словаря с произвольными элементами.

def dict_hash(slv):
    hash_value = 0
    for index, item in slv.items():
        # print(index, item)
        hash_value += hash(index)
        hash_value += hash(item)
    return hash_value % 10000


# Пример использования:
data = {"apple": 1, "banana": 2, "cherry": 3}
print(dict_hash(data))
