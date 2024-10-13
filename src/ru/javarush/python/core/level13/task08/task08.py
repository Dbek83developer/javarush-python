# Обработка ошибок запросов с модулем requests

# Напишите программу, которая отправляет GET-запрос на сервер и обрабатывает возможные ошибки, используя исключения.
import requests

try:
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    response.raise_for_status()  # Генерирует исключение для статус-кодов 4xx и 5xx
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"Other error occurred: {err}")
else:
    print("Success!")