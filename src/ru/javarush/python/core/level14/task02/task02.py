# Использование ThreadLocal

# Напишите программу, которая использует класс ThreadLocal для хранения данных, уникальных для каждого потока.

import threading

# Создание объекта ThreadLocal
local_data = threading.local()


def process_data():
    # Присвоение значения локальной переменной потока
    local_data.value = threading.current_thread().name
    # Доступ к локальной переменной потока
    print(f'Value in {threading.current_thread().name}: {local_data.value}')


threads = []
for i in range(5):
    t = threading.Thread(target=process_data)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
