# Создание сокет-сервера

# Напишите программу, которая создает сокет-сервер, принимает входящие соединения от клиентов и отвечает им "Hello, client!".

import socket

# Создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Связывание сокета с адресом и портом
server_socket.bind(('localhost', 12345))

# Прослушивание входящих соединений
server_socket.listen(5)
print("Сервер ожидает соединения...")

while True:
    # Принятие нового соединения
    client_socket, client_address = server_socket.accept()
    print(f"Соединение установлено с {client_address}")

    # Получение данных от клиента
    data = client_socket.recv(1024)
    print(f"Получено: {data.decode('utf-8')}")

    # Отправка данных клиенту
    client_socket.sendall(b'Hello, client!')

    # Закрытие соединения с клиентом
    client_socket.close()