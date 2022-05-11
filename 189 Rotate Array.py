# O(1) Space and Time
# [1,2,3,4,5,6], k = 2
# reverse array
# [6,5,4,3,2,1]
# reverse last n-k elements
# [6,5,1,2,3,4]
class Solution:
    def inplacereverse(self,nums,left,right):
        while left < right:
            nums[left],nums[right]=nums[right],nums[left]
            left,right=left+1,right-1
            
    def rotate(self, nums: List[int], k: int) -> None:
        # in place reversal
        nums.reverse()
        # array rotated by n is just same array
        n = len(nums)
        k = k % n
        # reverse all elements
        Solution.inplacereverse(self,nums,0,k-1)
        # reverse last n-k elements
        Solution.inplacereverse(self,nums,k,len(nums)-1)    
            