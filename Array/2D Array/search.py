import numpy as np

arr = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])

print(arr)

def search2array(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == target:
                return i, j
    return -1

print(search2array(arr, 6)) # (1, 2)
print(search2array(arr, 0)) # -1