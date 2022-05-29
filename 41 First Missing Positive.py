# The first missing +ve needs to be in first n positions
from calendar import c


class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        # similar to array technique, go to nums[value]
        for i in range(n):
            correctPos = nums[i] - 1
            while 1 <= nums[i] <= n and nums[i] != nums[correctPos]:
                nums[i], nums[correctPos] = nums[correctPos], nums[i]
                correctPos = nums[i] - 1
        
        for i in range(n):
            if i+1 != nums[i]:
                return i+1
        return n+1
        
