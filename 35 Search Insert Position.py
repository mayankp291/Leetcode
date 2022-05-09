class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lower = 0
        upper = n - 1
        mid = 0
        while lower <= upper:
            mid = int(lower + (upper - lower) / 2)
            curr = nums[mid]
            if curr == target:
                return mid
            if curr < target:
                lower = mid + 1
            else:
                upper = mid - 1
        if nums[mid] > target:
            return mid
        return mid + 1
