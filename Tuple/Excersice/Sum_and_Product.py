def sum_product(input_tuple):
    # TODO
    sum = 0
    product = 1
    for element in input_tuple:
        sum  = element + sum
        product = element * product
        
    return sum, product
