# Отправка GET-запроса
import requests
# Напишите программу, которая отправляет GET-запрос с параметрами на URL и обрабатывает полученный JSON-ответ.

params = {'userId': 1}
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
print(response.json())