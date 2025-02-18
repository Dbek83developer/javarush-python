# Выполнение POST-запроса с использованием http.client

# Напишите программу, которая выполняет POST-запрос на сервер с передачей данных и выводит ответ.
# Программа должна обрабатывать возможные ошибки.

import http.client
import json
try:
    # Данные для отправки
    payload = json.dumps({
        "title": "foo",
        "body": "bar",
        "userId": 1
    })

    # Заголовки
    headers = {
        'Content-Type': 'application/json'
    }

    # Создание подключения
    conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")

    # Отправка POST-запроса
    conn.request("POST", "/posts", body=payload, headers=headers)

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
