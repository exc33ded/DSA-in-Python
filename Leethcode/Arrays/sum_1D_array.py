# 1480. Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        lst = []
        for i in range(len(nums)):
            lst.append(nums[i] + sum)
            sum += nums[i]
        return lst
