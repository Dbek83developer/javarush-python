import time
# import numpy as np


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def measure_time(search_func, arr, target):
    start_time = time.time()
    search_func(arr, target)
    end_time = time.time()
    return end_time - start_time


n = 20
target = -1  # Target that is not in the array to ensure full search
threshold_found = False

for i in range(n + 1):
    arr_length = 2 ** i
    arr = list(range(arr_length))  # Sorted array for binary search
    linear_time = measure_time(linear_search, arr, target)
    binary_time = measure_time(binary_search, arr, target)

    print(f"Array length: {arr_length}, Linear search time: {linear_time:.12f}, Binary search time: {binary_time:.12f}")

    if binary_time < linear_time and not threshold_found:
        print(f"Binary search becomes more efficient at array length: {arr_length}")
        threshold_found = True
        break

if not threshold_found:
    print("Binary search did not become more efficient within the given range.")