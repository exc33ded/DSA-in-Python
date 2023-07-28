# 3 methods of insertion in list

lst = [1,2,3,4,5,6,7,8,9,10]

# using 'insert(index, element)'
lst1 = lst
lst1.insert(0, 11)
print(lst1) # [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# using 'append(element)' <-- insetion at the end of the list
lst2 = lst
lst2.append(55) 
print(lst2) # [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55]

# using extend(list2) <-- concat another list
lst2 = [11,12,13,14,15]
lst.extend(lst2) 
print(lst) # [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55, 11, 12, 13, 14, 15]
