# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))
