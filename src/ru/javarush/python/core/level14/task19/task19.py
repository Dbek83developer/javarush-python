# Использование многопроцессорности

# Напишите программу, которая создает 4 параллельных процесса.
# Каждый процесс должен печатать свое имя и текущий идентификатор процесса.
# Используйте модуль multiprocessing.
import multiprocessing
import os


def worker(num):
    print(f'{os.getpid()} Process{num}')


def main():
    processes = []
    for i in range(4):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

main()
