# Дерево файлов

# Напишите рекурсивный алгоритм для обхода дерева файлов.
# Алгоритм должен обходить каталог и все его подкаталоги, выводя список всех файлов и папок.

import os

def traverse_directory(path):
    # Получаем список всех файлов и папок в текущем каталоге
    items = os.listdir(path)
    # indent = 0

    for item in items:
        # Создаём полный путь к файлу или папке
        path = os.path.join(path, item)

        # Выводим с отступом для лучшего восприятия структуры
        # print(' ' * indent + item)
        print(item)

        # Если это папка, рекурсивно обходим её содержимое
        if os.path.isdir(path):
            # indent += 4
            traverse_directory(path)


# Пример использования
start_path = 'C:/Users/user/Downloads/Telegram Desktop'  # Замените на нужный путь
traverse_directory(start_path)