# Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.

def get_diagonal(tup):
    lst = []
    # TODO
    for i in range(len(tup)):
            lst.append(tup[i][i])
            
    return tuple(lst)
