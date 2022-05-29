# Time O(n) Space O(1)
# Prefix of a num is the * of all nums before it, postfix * of all nums after it
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = n * [1]
        temp = 1

        # store prefix in ans (left to right)
        for i in range(0, n):
            ans[i] = temp
            temp*=nums[i]
        print(ans)

        # multiply by postfix in ans (right to left)
        temp = 1
        for j in range(n - 1, -1, -1):
            ans[j] *= temp
            temp*=nums[j]
        print(ans)
        return ans
        

Solution.productExceptSelf(Solution, [1,2,3,4])