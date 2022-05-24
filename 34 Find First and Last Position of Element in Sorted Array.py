# Binary Search twice
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # if arr is empty
        if len(nums) == 0:
            return [-1,-1]
        # find leftmost index
        l, r = 0, len(nums)-1
        left = -1
        right = -1
        while l<=r:
            mid = l + (r-l)//2
            curr = nums[mid]
            if curr < target:
                l = mid + 1
            elif curr > target:
                r = mid - 1
            else:
                left = mid
                r = mid - 1
        # find rightmost index
        l, r = left, len(nums)-1
        while l<=r:
            mid = l + (r-l)//2
            curr = nums[mid]
            if curr < target:
                l = mid + 1
            elif curr > target:
                r = mid - 1
            else:
                right = mid
                l = mid + 1
        
        return [left, right]
        