# 1920. Build Array from Permutation
# Try for TC : O(1) ?? 

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            ans.append(nums[nums[i]])

        return ans
