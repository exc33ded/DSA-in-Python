# Write a program to find all the pairs of integers whose sum is equal to a given integer.

def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(nums[i], nums[j])
                
findPairs([1,2,3,2,3,4,5,6], 6) 

# Leethcode Solution

def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
 
nums = [2, 7, 11, 15]
target = 9
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")

# Time Complexity is O(1)