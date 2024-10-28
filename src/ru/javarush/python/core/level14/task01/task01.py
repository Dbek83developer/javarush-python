# Использование класса Timer
import threading
# Напишите программу, которая использует класс Timer для выполнения функции с задержкой
# и демонстрирует отмену таймера до его срабатывания.


def greeting():
    print("Salom")


t = threading.Timer(5, greeting)
t.start()

# stop
t.cancel()
