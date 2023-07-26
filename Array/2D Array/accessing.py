import numpy as np

arr = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])

def accessElement(arr, row, col):
    if row >= len(arr) or col >= len(arr[0]):
        print('Incorrect Index')
    else:
        print(arr[row][col])

accessElement(arr, 2, 2)