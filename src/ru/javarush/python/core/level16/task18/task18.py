# Авторизация
import hashlib

# Напишите программу имитации логина пользователей.
# Программа должна содержать функцию login(email, password) и register(email, password).
# При регистрации пользователя нужно вызвать функцию register и добавить пользователя в список пользователей.
# Вместо пароля нужно хранить его hash.
# При логине пользователя нужно вызвать функцию login где проверить, что hash пароля совпадает с одним из сохраненных хешей.

users = {}


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register(email, password):
    hashed_password = hash_password(password)
    users[email] = hashed_password
    print(f"User {email} registered successfully.")


def login(email, password):
    if email in users and users[email] == hash_password(password):
        print(f"User {email} logged in successfully.")
    else:
        print("Login failed: Invalid email or password.")


# Example usage
register("user@example.com", "securepassword123")
login("user@example.com", "securepassword123")
login("user@example.com", "wrongpassword")