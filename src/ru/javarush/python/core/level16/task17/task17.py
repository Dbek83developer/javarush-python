# Хеширование паролей
import hashlib


# Напишите программу для хеширования паролей.
# Ваша задача — создать функцию, которая принимает строку пароля и возвращает его хеш-значение.

def hash_password(password: str) -> str:
    return hashlib.sha3_256(password.encode()).hexdigest()


# Пример использования:
password = "my_secure_password"
hashed_password = hash_password(password)
print(hashed_password)
