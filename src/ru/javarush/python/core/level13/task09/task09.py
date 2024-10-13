# Выполнение GET-запроса с использованием http.client

# Напишите программу, которая выполняет GET-запрос на сервер, читает и выводит ответ.
# Программа должна обрабатывать возможные ошибки.

import http.client

try:
    # Создание подключения
    conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")

    # Отправка GET-запроса
    conn.request("GET", "/posts/1")

    # Получение ответа
    response = conn.getresponse()
    print(response.status, response.reason)

    # Чтение и декодирование данных ответа
    data = response.read().decode('utf-8')
    print(data)

except http.client.HTTPException as e:
    print("HTTP error occurred:", e)
except Exception as e:
    print("An error occurred:", e)
finally:
    # Закрытие подключения
    conn.close()