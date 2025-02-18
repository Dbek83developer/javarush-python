# Параллельное суммирование

# Напишите программу, которая использует параллельное программирование для суммирования элементов большого массива.
# Разделите массив на несколько частей и используйте несколько процессов для одновременного суммирования.
# Подсказка: Используйте модуль multiprocessing в Python для создания нескольких процессов.
# Разделите массив на подмассивы и вычисляйте их суммы параллельно, а затем объедините результаты.


import multiprocessing


def partial_sum(array_slice):
    return sum(array_slice)


if __name__ == "__main__":
    # num_processes = 0
    array = [i for i in range(1, 1000001)]  # Большой массив для суммирования
    num_processes = multiprocessing.cpu_count()  # Число доступных процессоров
    print(num_processes)
    # Разделяем массив на равные части
    chunk_size = len(array) // num_processes
    chunks = [array[i * chunk_size: (i + 1) * chunk_size] for i in range(num_processes)]

    # Создаем пул процессов
    with multiprocessing.Pool(processes=num_processes) as pool:
        # Вычисляем сумму каждой части параллельно
        partial_sums = pool.map(partial_sum, chunks)

    # Объединяем результаты
    total_sum = sum(partial_sums)

    print(f"Total sum: {total_sum}")
