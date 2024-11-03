import array

# Define dimensions
rows, cols = 10, 10

# Create a 1D array with a size of rows * cols, initialized with zeros
two_d_array = array.array('i', [0] * (rows * cols))

# Function to get value at (row, col)
def get_value(row, col):
    return two_d_array[row * cols + col]

# Function to set value at (row, col)
def set_value(row, col, value):
    two_d_array[row * cols + col] = value

# Example usage
for i in range(1, 11):
    for j in range(1, 11):
        set_value(i-1, j-1, i*j)  # Set the element at row 1, column 1 to 5
# set_value(0, 2, 3)  # Set the element at row 0, column 2 to 3

# Print the 2D array in a table format
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{get_value(i-1, j-1):3}", end=" ")
    print()  # Newline after each row