# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

def pair_sum(myList, sum):
    lst = []
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] == sum:
                lst.append(f'{myList[i]}+{myList[j]}')
                
    return lst