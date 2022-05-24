class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # O(m*n) Time
        ans = 0
        for i in arr1:
            count = 1
            for j in arr2:
                if abs(i-j) <= d:
                    count = 0
                    break
            ans+=count
        return ans