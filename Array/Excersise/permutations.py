def permutations(num):
    if num < 0:
        print('Permutation of ', num, 'is not defined!!')
    elif num == 1 or num == 0:
        print(1)
    else:
        print(permutations(num)*permutations(num-1))
        
permutations(5)