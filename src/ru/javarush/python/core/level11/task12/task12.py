# Перегрузка операторов индексации

# Напишите класс Matrix, который будет представлять двумерную матрицу и поддерживать перегрузку операторов индексации ([]).
# Реализуйте методы __getitem__ и __setitem__.

class Matrix:
    def __init__(self, rows, cols):
        # Initialize a matrix with given rows and columns filled with zeros (or any default value)
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, index):
        try:
            i, j = index  # Unpack the tuple (i, j)
            return self.data[i][j]
        except IndexError as e:
            return f"IndexError: {e}"

    def __setitem__(self, index, value):
        try:
            i, j = index  # Unpack the tuple (i, j)
            self.data[i][j] = value
        except IndexError as e:
            return f"IndexError: {e}"


# Example usage
matrix = Matrix(3, 3)  # Create a 3x3 matrix
matrix[0, 0] = 1       # Set value at position (0, 0)
print(matrix[0, 0])    # Output: 1
