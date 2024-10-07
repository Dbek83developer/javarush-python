# Сериализация помощью pickle
import pickle
# Напишите программу, которая сериализует и десериализует объект Python с использованием модуля pickle.
# Объектом для сериализации будет словарь, содержащий информацию о студенте: имя, возраст и статус студента.

# Напишите тут ваш код

# Объект для сериализации
student_info = {
    'name': 'John Doe',
    'age': 20,
    'status': 'student'
}

# Сериализация объекта в файл
with open('data.pkl', 'wb') as file:
    pickle.dump(student_info, file)

# Десериализация объекта из файла
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
