# Двоичное представление

# Напишите программу, которая принимает целое число от пользователя,
# преобразует его в двоичное представление и показывает, как оно будет храниться в памяти.
# В программе также должно быть отображено количество байтов, занимаемое числом.

# Get integer input from the user
number = int(input("Enter an integer: "))

# Convert the integer to binary
binary_representation = bin(number)[2:]  # Remove the '0b' prefix

# Format it to show as it might be stored in memory
# Add leading zeros to make it a multiple of 8 bits for better readability
bits = 8  # Number of bits per byte
formatted_binary = binary_representation.zfill((len(binary_representation) + bits - 1) // bits * bits)

# Split the binary representation into bytes (8-bit groups)
memory_representation = ' '.join(formatted_binary[i:i + bits] for i in range(0, len(formatted_binary), bits))

# Define the number of bytes to use (e.g., 2 or 4 for demonstration purposes)
num_bytes = (number.bit_length() + 7) // 8  # Calculates minimum bytes needed

# Convert the number to bytes
byte_representation = number.to_bytes(num_bytes, byteorder='big')

# Display the result
print(f"Binary representation of {number}:")
print(memory_representation)
print(num_bytes)
# print(number.bit_count())
