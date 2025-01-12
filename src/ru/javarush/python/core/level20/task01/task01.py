# Количество элементов

# Напиши функцию, которая пройдет по массиву и подсчитает сколько каких элементов встречается.

def count_elements(arr):
    n = len(arr)
    # count = 0
    slv = {}
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        if not arr[i] in slv.keys():
            slv[arr[i]] = count

    return slv

# Пример использования:
arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(count_elements(arr))  # Output: {1: 1, 2: 2, 3: 3, 4: 4}