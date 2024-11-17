# Мемеоизация Фибоначчи

# Напишите функцию для вычисления n-го числа Фибоначчи с использованием мемоизации,
# чтобы улучшить производительность по сравнению с простым рекурсивным подходом.


def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# Пример использования
n = 10
print(f"fibonacci_memo({n}) = {fibonacci_memo(n)}")
