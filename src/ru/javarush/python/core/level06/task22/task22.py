# Перегруппировка.

# Напишите программу, которая принимает строку из нескольких слов, разделенных запятыми, от пользователя.
# Программа должна:
# Разделить строку на список слов с использованием метода split().
# Объединить этот список слов в одну строку с использованием метода join(), разделив слова пробелами.
# Вывести результаты каждой операции.

# Напишите тут ваш код
try:
    text = input("Enter the words with comma: ")
    list_word = text.split(',')
    joined = ' '.join(list_word)
    print(list_word)
    print(joined)
except:
    print('Error')