# Хеш-функция

# Напиши свою хеш-функцию, которая возвращает целое число от 0 до 10к для строки произвольной длинны.

def custom_hash(word):
    a = 31
    m = 10000
    hash_value = 0
    for char in word:
        hash_value = (hash_value * a + ord(char)) % m
    return hash_value


# Пример использования:
key = "example"
print(f"Хеш-значение для ключа '{key}': {custom_hash(key)}")
