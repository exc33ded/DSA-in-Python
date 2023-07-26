import numpy as np

arr = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])

new2array = np.insert(arr, 0, [[10,11,12]], axis=1)
print(new2array)

# [[10  1  2  3]
#  [11  4  5  6]
#  [12  7  8  9]]

new2array = np.insert(arr, 0, [[13,14,15]], axis=0)
print(new2array)

# [[13 14 15]
#  [ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]]