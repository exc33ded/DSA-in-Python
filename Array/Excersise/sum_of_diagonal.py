# Calculate the sum of diagonal elements.

myList2D= [[1,2,3],[4,5,6],[7,8,9]]

def diagonal_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum = matrix[i][i] + sum 
    
    return sum

print(diagonal_sum(myList2D))