# Time O(n), Space O(n)
# use hashing to and check the longest subsequence
# Ex: nums = [100,4,200,1,3,2]
# can be divided into 100, 200, 1->2->3->4
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        length = 0
        for num in nums:
            # check if predecessor of a number is in set, 
            # then it cannot be start of a subsequence
            if (num - 1) not in nums:
                length = 0
                # check if it has consecutive numbers
                while (num + length) in nums:
                    length += 1
                ans = max(length, ans)
        return ans
