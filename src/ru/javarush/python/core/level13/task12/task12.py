# Использование прокси-сервера с модулем http.client

# Напишите программу, которая отправляет GET-запрос через прокси-сервер с использованием библиотеки http.client.
import http.client

# Настройки прокси-сервера
proxy_host = '10.10.1.10'
proxy_port = 3128
dest_url = 'httpbin.org'
dest_path = '/ip'

# Создание соединения с прокси-сервером
conn = http.client.HTTPConnection(proxy_host, proxy_port)

# Формирование и отправка запроса
conn.set_tunnel(dest_url)
conn.request('GET', dest_path)

# Получение ответа
response = conn.getresponse()
print(response.status, response.reason)
print(response.read().decode('utf-8'))

# Закрытие соединения
conn.close()
