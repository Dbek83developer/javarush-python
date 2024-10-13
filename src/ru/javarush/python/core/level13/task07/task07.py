# Обработка ответов сервера с модулем requests
import requests
# Напишите программу, которая отправляет GET-запрос на сервер и обрабатывает ответ, включая статус-код, заголовки и тело ответа.
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(response.status_code)
print(response.headers)  # Выводит заголовки ответа
print(response.headers['Content-Type'])
print(response.content)

