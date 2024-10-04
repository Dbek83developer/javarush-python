# Переупаковка исключения

# Напишите функцию validate_input, которая принимает строку и проверяет,
# что она не пустая и что ее длина не превышает 10 символов.
# Если строка пустая, запустите ValueError с сообщением "Input cannot be empty".
# Если строка слишком длинная, запустите ValueError с сообщением "Input is too long".
# Затем перехватите это исключение и переупакуйте его в пользовательское исключение InputValidationError, сохранив исходное исключение как причину.
class InputValidationError(Exception):
    def __init__(self, original_exception):
        super().__init__()
        self.original_exception = original_exception


def validate_input(txt):
    try:
        if txt == "":
            raise ValueError("Input cannot be empty")
        elif len(txt) > 10:
            raise ValueError("Input is too long")
    except ValueError as e:
        raise InputValidationError from e


# Пример использования:
try:
    validate_input("")
except InputValidationError as e:
    print(f"Caught custom exception: {e}")
    print(f"Original exception: {e.original_exception}")