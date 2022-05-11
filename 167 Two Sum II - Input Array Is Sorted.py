# O(logn) Time, O(1) Space
# 2 pointer binary search type 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            res = nums[l] + nums[r]
            if res == target:
                return [l + 1, r + 1]
            elif res < target:
                l = l + 1
            else:
                r = r - 1