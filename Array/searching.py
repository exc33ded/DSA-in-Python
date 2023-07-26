from array import *

arr = array('i', [1,2,3,4,5,6,7,8,9,10])
target = int(input('Enter element to search: '))

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search(arr, target))