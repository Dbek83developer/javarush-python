# Преобразуем число в десятичное
# Напишите программу, которая принимает двоичное целое число от пользователя,
# преобразует его в десятичное представление и показывает, как оно будет храниться в памяти.
# В программе также должно быть отображено количество байтов, занимаемое числом.
# Get binary input from the user
binary_input = input("Enter a binary number (e.g., 1010): ")

# Convert binary string to decimal integer
decimal_number = int(binary_input, 2)

# Calculate the number of bytes needed to store the decimal number
num_bytes = (decimal_number.bit_length() + 7) // 8  # Each byte is 8 bits

# Convert the decimal number to bytes
byte_representation = decimal_number.to_bytes(num_bytes, byteorder='big')  # 'big' for big-endian format

# Display the results
print(f"Binary input: {binary_input}")
print(f"Decimal representation: {decimal_number}")
# print(f"Byte representation in memory: {byte_representation}")
print(f"Number of bytes required: {num_bytes}")

