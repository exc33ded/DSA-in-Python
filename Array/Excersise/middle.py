# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

myList = [1, 2, 3, 4]

def middle(lst):
    # TODO
    del lst[0]
    del lst[-1]
    
    return lst

print(middle(myList))