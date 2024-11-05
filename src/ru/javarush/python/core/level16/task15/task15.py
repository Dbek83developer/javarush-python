# Сумма чисел

# Дан массив чисел и целевое значение суммы. Необходимо найти все пары чисел, которые в сумме дают целевое значение.

def find_pairs(nums, target):
    seen = set()
    pairs = []
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs


# Пример использования
nums = [2, 4, 3, 5, 7, 8, 9]
target = 10
print(find_pairs(nums, target))