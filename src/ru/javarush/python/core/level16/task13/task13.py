def find_duplicates(arr):
    seen = set()
    duplicates = []
    for item in arr:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates


# Пример использования:
nums = [1, 2, 3, 2, 4, 5, 6, 3, 7, 8, 1]
print(find_duplicates(nums))  # Output: [2, 3, 1]