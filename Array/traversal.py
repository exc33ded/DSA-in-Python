from array import *

lst = []
index = int(input("Enter the number of elemenets to insert: "))
for i in range(index):
    ele = int(input("> "))
    lst.append(ele)
arr = array('i', lst)

# Traversing 
for i in arr:
    print(i)