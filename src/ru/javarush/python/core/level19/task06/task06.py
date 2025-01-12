# Большой подмассив

# Дан массив длинны n состоящий из целых чисел.
# Найти минимальный подмассив с суммой элементов, превышающей заданное значение S.


def min_subarray_len(s, nums):
    n = len(nums)
    min_len = n + 1
    left = 0
    curr_sum = 0

    for right in range(n):
        curr_sum += nums[right]
        # print(f"right {curr_sum}")
        while curr_sum >= s:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            # print(curr_sum)
            left += 1

    return 0 if min_len == n + 1 else min_len



# Пример использования
arr = [2, 3, 1, 2, 4, 3]
S = 7
print(min_subarray_len(S, arr))  # Output: 2 (подмассив [4, 3])