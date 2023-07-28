# Write a function to find the missing number in a given integer array of 1 to 100.


def missing_number(arr, n):
    # TODO

    # Thinking process
    # Sum of all the elements in the array, when subtracted with the array with the missing element
    # will result in getting the missing number
    
    # Getting the sum of the array present
    sum = 0
    for ele in arr:
        sum = ele + sum
    sum_of_given_array = sum
    
    # Getting sum of 'n' elements
    sum2 = 0
    for i in range(1, n+1):
        sum2 = i + sum2
    sum_of_generated_array = sum2
    
    # Missing number
    return int(sum_of_generated_array - sum_of_given_array)