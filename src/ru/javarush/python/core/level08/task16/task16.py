# Платформа.
import platform
# Напишите программу, которая получает и выводит информацию о текущей операционной системе
# и платформе с помощью библиотеки platform. Программа должна:
# Получить и вывести имя операционной системы.
# Получить и вывести имя компьютера в сети (hostname).
# Получить и вывести версию операционной системы.
# Получить и вывести архитектуру процессора.
# Получить и вывести версию Python.

# Напишите тут ваш код
print("Operating System:", platform.system())
print("Node Name:", platform.node())
# print("OS Release:", platform.release())
print("OS Version:", platform.version())
# print("Machine:", platform.machine())
print("Processor:", platform.processor())
print("Architecture:", platform.architecture())
print("Python Version:", platform.python_version())
# print("Python Compiler:", platform.python_compiler())