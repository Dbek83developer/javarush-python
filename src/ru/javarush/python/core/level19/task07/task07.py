# Размен моент

# У нас есть монеты разного номинала. Нужно найти минимальное количество монет для сдачи заданной суммы.
# Подсказка: Всегда берется монета с наибольшим номиналом, не превышающим оставшуюся сумму.


def min_coins(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count


# Пример использования
coins = [1, 2, 5, 10, 25]
amount = 63
print(min_coins(coins, amount))  # Вывод: 5 (25 + 25 + 10 + 2 + 1)