# Частота слов

# Напишите функцию для подсчета частоты каждого слова в тексте.
# Используйте оптимальную структуру данных для хранения частоты слов.
from collections import Counter


def word_frequency(text):
    words = text.split()
    print(words)
    frq = Counter(words)
    return frq


# Пример использования функции
text = "Напишите функцию для подсчета частоты каждого слова в тексте."
print(word_frequency(text))
