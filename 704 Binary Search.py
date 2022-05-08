from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lower = 0
        upper = n-1
        while lower <= upper:
            mid = int(lower + (upper-lower)/2)
            curr = nums[mid]
            if curr == target:
                return mid
            if curr < target:
                lower = mid + 1
            else:
                upper = mid - 1
        return -1

print(Solution.search(Solution, [-1,0,3,5,9,12], 9))

