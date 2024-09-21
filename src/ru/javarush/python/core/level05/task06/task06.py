# Поиск строки

# Напишите программу, которая создает список из 10 элементов.
# Программа просит пользователя ввести строку, а потом проверяет - есть она в списке или нет.

# Напишите тут ваш код
my_list = ["non", "olma", "nok", "pishloq", "moloko", "novvot", "malina", "tut", "tort", "shkolad"]
word = input("Enter the word: ")
if word in my_list:
    print(True)
else:
    print(False)