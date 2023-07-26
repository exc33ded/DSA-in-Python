from array import *

print("1. Create an array and traverse")
arr = array('i', [1,2,3,4,5,6,7,8,9,10])
for i in arr:
    print(i, end=' ')
print()

print("2. Access individual element through indexes")
for i in range(len(arr)):   
    print(arr[i])

print("3. Append any value to the array using 'append()'")
arr.append(11)
print(arr)

print("4. Extend an array using 'extend()'")
arr_new = array('i', [11,12,13,14,15,16,17,18,19,20])
arr.extend(arr_new)
print(arr)

print("5. Add items from the list using 'fromlist()'")
lst = [1,2,15,5,8,9,6,3,26]
arr.fromlist(lst)
print(arr)

print("6. Remove any array element using 'remove()'")
arr.remove(26)
print(arr)

print("7. Remove last array element using 'pop()'")
arr.pop()
print(arr)

print("8. Fetch any element from it's index using 'index()'")
print(arr.index(5))

print("9. Reverse a python array using 'reverse()'")
arr.reverse()
print(arr)

print("10. Get array buffer information using 'buffer_info()'")
print(arr.buffer_info())

print("11. Check the number of occurences using 'count()'")
print(arr.count(5))

print("12. Convert array to string using 'tobytes()'")
str = arr.tobytes()
print(str)
ints = array('i')
ints.frombytes(str)
print(ints)

print("13. Convert array to list using 'tolist()'")
print(arr.tolist())

print("14. Append a string to char array using 'fromstring()'")


print("15. Slice Elements from an array")
print(arr[4::2])

print("16. Insert any value in the array using 'insert()'")
arr.insert(0, 12)
print(arr)