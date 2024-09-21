# Три проверки.

# Напишите программу, которая создает словарь с информацией о книге (например, название, автор, год издания).
# Программа должна:
# Проверить наличие ключа "author" с использованием оператора in.
# Проверить наличие ключа "publisher" с использованием метода get().
# Проверить наличие ключа "title" с использованием метода keys().

# Напишите тут ваш код
books = {"title": "Communication", "author": "Dayl Karnegi", "year": 1998}
if "author" in books:
    print(books["author"])
print(books.get("publisher"))
if "title" in books.keys():
    print(books["title"])
