# Разложение

# Найти количество способов разложить заданное число n на слагаемые.
# Подсказка: Если текущее слагаемое меньше или равно целевой сумме,
# количество способов = количество способов без текущего слагаемого + количество способов с текущим слагаемым.
def count_partitions(n, max_summand):
    if n == 0:
        return 1
    if n < 0 or max_summand == 0:
        return 0
    return count_partitions(n, max_summand - 1) + count_partitions(n - max_summand, max_summand)


def number_of_ways(n):
    return count_partitions(n, n)


n = int(input("Введите число n: "))
print("Количество способов разложить число", n, "на слагаемые:", number_of_ways(n))