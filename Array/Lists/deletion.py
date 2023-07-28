# 3 methods to delete elements in a list

lst = [1,2,3,4,5,6,7,8,9,10]

# using 'pop()' <--- if index is specified it removes specific element in the given index / if not it removes last element
lst.pop()
lst.pop(0)
print(lst) # [2, 3, 4, 5, 6, 7, 8, 9]

# using 'remove(element)' <-- it removes the given element from the list
lst.remove(5) 
print(lst) # [2, 3, 4, 6, 7, 8, 9]

# using del operation <-- remove slice in a list
del lst[2:4]
print(lst) # [2, 3, 7, 8, 9]