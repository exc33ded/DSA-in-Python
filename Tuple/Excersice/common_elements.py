# Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))
