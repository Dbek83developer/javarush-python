# Палиндром

# Написать наивный метод для проверки, является ли строка палиндромом (читается одинаково в обоих направлениях).


def is_palindrome(s: str) -> bool:
    if s == s[::-1]:
        return True
    else:
        return False


# Пример использования:
example = "radar"
print(is_palindrome(example))  # True