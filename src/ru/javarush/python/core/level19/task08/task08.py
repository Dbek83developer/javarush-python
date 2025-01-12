# Задача о рюкзаке с дроблением

# У нас есть предметы с известной стоимостью и весом. Мы хотим положить в рюкзак фиксированного размера вещей на как можно большую сумму.
# Предметы можно делить на части.
# Подсказка: Сортировка предметов по удельной стоимости (стоимость/вес) и выбор наибольших удельных стоимостей до заполнения рюкзака.


def fractional_knapsack(values, weights, capacity):
    udel = list()
    total = 0
    for i in range(len(weights)):
        udel.append((values[i]/weights[i], values[i], weights[i]))
    udel.sort(reverse=True)
    for item in udel:
        if capacity >= item[2]:
            total += item[1]
            capacity -= item[2]
        else:
            total += item[0] * capacity
            break
    return total



# Пример использования
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print(fractional_knapsack(values, weights, capacity))