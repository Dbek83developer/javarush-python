# Создание сокет-клиента

# Напишите программу, которая создает сокет-клиента, подключается к сокет-серверу, отправляет ему сообщение и получает ответ.
import socket
try:
    # Создание сокета
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Установка соединения с сервером
    client_socket.connect(('localhost', 12345))

    # Отправка данных на сервер
    client_socket.sendall(b'Hello, server!')

    # Получение данных от сервера
    data = client_socket.recv(1024)
    print(f"Получено от сервера: {data.decode('utf-8')}")
except Exception as e:
    print(e)
finally:
    # Закрытие сокета
    client_socket.close()