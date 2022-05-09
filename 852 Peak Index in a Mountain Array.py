class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        n = len(nums)
        lower = 0
        upper = n-1
        while lower <= upper:
            mid = int(lower + (upper-lower)/2)
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            # increasing slope
            elif nums[mid-1] < nums[mid] < nums[mid+1]:
                lower = mid
            # decreasing slope
            elif nums[mid-1] > nums[mid] > nums[mid+1]:
                upper = mid
        return -1