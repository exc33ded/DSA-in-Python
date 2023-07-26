import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search(arr, 5))
print(linear_search(arr, 0))
