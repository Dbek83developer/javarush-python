# Путь в графе

# У вас есть граф, представленный в виде матрицы смежности, где graph[i][j] обозначает стоимость пути от города i к городу j.
# Найдите минимальный путь, который начинается и заканчивается в одном и том же городе и проходит через все города ровно один раз
# Подсказка: Используйте динамическое программирование для хранения промежуточных результатов.

INF = float('inf')
def tsp(graph):
    n = len(graph)
    dp = [[None] * (1 << n) for _ in range(n)]
    start = 0

    def visit(city, visited):
        if visited == (1 << n) - 1:
            return graph[city][start]
        if dp[city][visited] is not None:
            return dp[city][visited]
        result = float('inf')
        for next_city in range(n):
            if visited & (1 << next_city) == 0:
                result = min(result, graph[city][next_city] + visit(next_city, visited | (1 << next_city)))
        dp[city][visited] = result
        return result

    return visit(start, 1 << start)


# Пример использования
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print(tsp(graph))