# Использование прокси-сервера с модулем requests

# Напишите программу, которая отправляет GET-запрос через прокси-сервер с использованием библиотеки requests.
import requests

# URL-адрес, к которому выполняется запрос
url = 'http://httpbin.org/ip'

# Настройки прокси-сервера
proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
}

# Отправка GET-запроса через прокси
response = requests.get(url, proxies=proxies)

print(response.json())
