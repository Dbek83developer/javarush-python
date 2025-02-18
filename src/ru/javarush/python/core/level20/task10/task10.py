# Жадный коммивояжер
# Напишите программу для решения задачи коммивояжера с использованием жадного алгоритма ближайшего соседа.

# Хотя этот метод не гарантирует оптимальное решение, он может найти хорошее решение за полиномиальное время.
# Подсказка: Начните с любого города и последовательно переходите в ближайший ещё не посещенный город, пока не будут посещены все города.

import math


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)


def nearest_neighbor(cities):
    n = len(cities)
    start_city = cities[0]
    unvisited = cities[1:]
    current_city = start_city
    route = [start_city]

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        route.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    route.append(start_city)
    return route


# Пример использования
cities = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
path = nearest_neighbor(cities)
print("Путь коммивояжера:", path)