# Отправка POST-запроса

# Напишите программу, которая отправляет POST-запрос с JSON-данными на URL и обрабатывает полученный JSON-ответ.
import requests

data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print(response.status_code)
print(response.json())
