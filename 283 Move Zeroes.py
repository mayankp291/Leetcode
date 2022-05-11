# quicksort like technique (using 2 pointers) to seperate array into 2 containers.
# left side non-zero, right zero numbers
# start both pointer at 0 and move r, swap when r is non-zero
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l, r = 0, 0
        while r < len(nums):
            # non zero nums[r]
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        
            
