class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = True
        decrease = True

        for i in range(0, (len(nums)-1)):   # O(n)
            if (nums[i] < nums[i+1]):  #O(1)
                decrease = False
            if (nums[i] > nums[i+1]): # O(1)
                increase = False
            
        return increase or decrease
