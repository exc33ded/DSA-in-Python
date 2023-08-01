# arr = [1, 7, 3, 4, 9, 5]

arr = [1, 7, 3, 4, 9, 5]


def max_product(arr):
    
    max1, max2 = 0, 0
    
    for ele in arr:
        if ele > max1:
            max2 = max1
            max1 = ele
            
        elif ele > max2:
            max2 = ele
        
    return max1*max2

print(max_product(arr))