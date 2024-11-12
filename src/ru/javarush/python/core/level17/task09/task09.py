# Выход из лабиринта

# Дан двумерный массив, представляющий лабиринт, где 0 – это проходимая клетка, а 1 – стена.
# Напишите функцию для нахождения пути от начальной точки до конечной с использованием DFS.
# Начальная и конечная точки заданы координатами.

def find_path(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]
    visited = set()

    while stack:
        (x, y), path = stack.pop()
        if (x, y) == end:
            return path
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                stack.append(((nx, ny), path + [(nx, ny)]))

    return []



# Пример использования
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
end = (4, 4)
path = find_path(maze, start, end)
print(path)