# У вас есть набор предметов на складе заданный массивом картежей (вес, цена, количество).

# Вам нужно перевести их на другой склад, но каждого предмета можно взять не более чем k.
# Найти набор предметов, максимизирующий ценность.
# Подсказка 1:
# Используйте динамическое программирование для основной задачи о рюкзаке и жадные алгоритмы для удовлетворения дополнительных ограничений.
# Подсказка 2:
# 1) Создайте таблицу для хранения максимальных ценностей для каждого веса.
# 2) Обновляйте таблицу, учитывая ограничения на количество каждого предмета.
# 3) Используйте жадные методы для удовлетворения дополнительных ограничений, если необходимо.

def knapsack_with_restrictions(items, max_weight, k):
# Напишите тут ваш код


# Пример использования
items = [(2, 3, 4), (3, 4, 3), (4, 5, 2)]
max_weight = 10
k = 2
print(knapsack_with_restrictions(items, max_weight, k))  # Вывод максимальной ценности