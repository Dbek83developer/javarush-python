# Пользовательское исключение

# Создайте пользовательское исключение InvalidAgeError, которое будет вызываться в функции check_age,
# если возраст меньше 0 или больше 150. Обработайте это исключение в блоке try-except.

class InvalidAgeError(Exception):
    def __init__(self):
        super().__init__()


def check_age(yr):
    if yr < 0 or yr > 150:
        raise InvalidAgeError("Age is invalid")


try:
    age = int(input("Enter your age: "))
    check_age(age)
    print("Age is valid.")
except InvalidAgeError as e:
    print(e)
except ValueError:
    print("Please enter a valid integer for age.")
