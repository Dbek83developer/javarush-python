# Работа с директориями.
import os
# Напишите программу, которая создает директорию, переходит в нее, создает файл внутри этой директории,
# записывает в файл текст, а затем читает и выводит его содержимое.
# Программа должна:
# Создать директорию test_directory.
# Перейти в директорию test_directory.
# Создать файл test_file.txt и записать в него строку "Hello, World!".
# Прочитать содержимое файла test_file.txt и вывести его на экран.
# Удалить файл и директорию.

# Напишите тут ваш код
# Step 1: Create a new directory
directory = "test_directory"
if not os.path.exists(directory):
    os.mkdir(directory)  # Creates the directory if it doesn't exist

# Step 2: Create a new file and write "Hello World" in it
os.chdir(directory)
file_path = os.path.join("test_file.txt")
with open(file_path, "w") as file:
    file.write("Hello, World!")  # Write to the file

# Step 3: Open the file, read the content, and print it
with open(file_path, "r") as file:
    content = file.read()  # Read the content
    print(content)  # Print the content


# Step 4: Delete the file
if os.path.exists(file_path):
    os.remove(file_path)  # Removes the file
    print(f"File '{file_path}' has been deleted.")

# Step 5: Delete the directory
if os.path.exists(directory):
    os.rmdir(directory)  # Removes the directory and all its contents
    print(f"Directory '{directory}' has been deleted.")
