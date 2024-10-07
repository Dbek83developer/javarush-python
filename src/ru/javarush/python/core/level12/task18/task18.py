# Сериализация словаря в строку

# Напишите программу, которая сериализует словарь в строку с использованием модуля pickle,
# а затем десериализует этот словарь из строки.

import pickle

# Пример словаря для сериализации
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'Wonderland'
}

# Сериализация объекта в файл
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Десериализация объекта из файла
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)