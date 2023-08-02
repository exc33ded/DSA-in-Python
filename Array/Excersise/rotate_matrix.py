# Rotate Matrix/ Image - LeetCode 48
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

def rotate(matrix):
    print('Before Rotation: ', matrix)
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            # Swapping
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # reversing
    for row in matrix:
        row.reverse()
        
    return matrix
        
print(rotate(matrix=[[1,2,3],[4,5,6],[7,8,9]]))


# Explaination

# Transpose the matrix: a. for i in range(n): - Start a loop that iterates over the rows. b. for j in range(i, n): - Start a nested loop that iterates over the columns starting from the current row i. This ensures we only swap elements in the upper triangle of the matrix, avoiding double swaps. c. matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] - Swap the elements at positions (i, j) and (j, i).

# Reverse each row: a. for row in matrix: - Start a loop that iterates over each row in the matrix. b. row.reverse() - Reverse the elements in the current row.