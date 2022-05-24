class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        res = []
        n = len(nums)
        maxi = max(nums[0:k])
        res.append(maxi)
        for i in range(n-k):
            if nums[k+i] > maxi:
                maxi = nums[k+i]
                res.append(maxi)
            else:
                if nums[i] == maxi:
                    maxi = max(nums[i+1:i+k+1])
                    res.append(maxi)
                else:
                    res.append(maxi)
        return res