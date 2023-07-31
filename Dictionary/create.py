# 3 methods for dictioanry creation

# method 1
dict1 = dict({'one':'uno', 'two':'dos', 'three':'tres'})

# method 2
dict2 = {'one':'uno', 'two':'dos', 'three':'tres'} 

# method 3
tuple_dict = [('one', 'uno'), ('two', 'dos'), ('three', 'tres')]
dict3 = dict(tuple_dict)

print(dict1)
print(dict2)
print(dict3)