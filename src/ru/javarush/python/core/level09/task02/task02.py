# Создаем классы.

# Создайте класс Library с атрибутом books, который представляет собой список книг.
# Добавьте методы add_book(book) для добавления книги в библиотеку
# и display_books() для вывода списка всех книг.
# Создайте объект класса Library, добавьте несколько книг и выведите список книг, используя методы объекта.

# Напишите тут ваш код
class Library:
    books = ["Doston", "Ona", "Qushlar"]

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print(self.books)


shu = Library()
shu.add_book("Odamalr")
shu.add_book("Quron")
shu.display_books()