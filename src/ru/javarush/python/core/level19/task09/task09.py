# Задача о рюкзаке

# Имеется набор предметов, каждый с весом и стоимостью.
# Нужно выбрать предметы для рюкзака с грузоподъемностью w, чтобы максимизировать общую стоимость.
# Подсказка: Создается таблица, где строки соответствуют предметам, а столбцы — возможной вместимости рюкзака.
# Значение в ячейке представляет максимальную стоимость для данного числа предметов и вместимости.

def knapsack(weights, values, w):
    n = len(weights)
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    # print(dp)

    for i in range(1, n + 1):
        for capacity in range(1, w + 1):
            if weights[i - 1] <= capacity:
                dp[i][capacity] = max(dp[i - 1][capacity], dp[i - 1][capacity - weights[i - 1]] + values[i - 1])
            else:
                dp[i][capacity] = dp[i - 1][capacity]
    # print(dp)
    return dp[n][w]


# Пример использования:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
w = 5
print(knapsack(weights, values, w))  # Вывод: 7