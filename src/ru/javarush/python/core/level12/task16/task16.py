# Сериализация с помощью yaml
import yaml
# Напишите программу, которая сериализует и десериализует объект Python с использованием модуля yaml.
# Объектом для сериализации будет словарь, содержащий информацию о фильме: название, режиссёр и год выпуска.

# Напишите тут ваш код

# Пример словаря с информацией о фильме
film_info = {
    'title': 'Inception',
    'director': 'Christopher Nolan',
    'year': 2010
}

# Сериализация объекта в строку YAML
yaml_string = yaml.dump(film_info)
print(yaml_string)

# Сериализация объекта в файл YAML
with open('data.yaml', 'w') as file:
    yaml.dump(film_info, file)

# Десериализация объекта из строки YAML
loaded_data = yaml.load(yaml_string, Loader=yaml.FullLoader)
print(loaded_data)

# Десериализация объекта из файла YAML
with open('data.yaml', 'r') as file:
    loaded_data = yaml.load(file, Loader=yaml.FullLoader)
print(loaded_data)