# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def contains_duplicate(nums):
    lst = []
    for num in nums:
        if num in lst:
            return True
        else:
            lst.append(num)
    return False