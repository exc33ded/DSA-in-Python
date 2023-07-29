import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

def find_number(arr, to_find):
    for i in range(len(arr)):
        if arr[i] == to_find:
            return i
    return -1
    
print(find_number(arr, 5))
print(find_number(arr, 15))