# two sum solution using hashing
# Time O(n) Space O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = dict()
        for key, value in enumerate(nums):
            diff = target - value
            if diff in temp:
                return [key, temp[diff]]
            else:
                temp[value] = key
