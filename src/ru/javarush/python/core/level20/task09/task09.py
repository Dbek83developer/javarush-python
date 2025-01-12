# Полный перебор

# Напишите программу, которая находит подмножество массива, сумма элементов которого равна заданному числу, используя метод полного перебора.
# Подсказка: Используйте рекурсию для генерации всех возможных подмножеств массива и проверяйте, равна ли их сумма заданному числу.

def find_subsets(arr, target, index=0, current_subset=[]):
    # Base case: if target is met, print the current subset
    if sum(current_subset) == target:
        print(current_subset)
        return True
    if index >= len(arr):
        return False

    # Include the current element in the subset
    if find_subsets(arr, target, index + 1, current_subset + [arr[index]]):
        return True

    # Exclude the current element from the subset
    if find_subsets(arr, target, index + 1, current_subset):
        return True

    return False


# Примеры
arr = [3, 34, 4, 12, 5, 2]
target = 9
find_subsets(arr, target)
