class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        # O(n) Time
        # i = 0
        # while n-i>0:
        #     i+=1
        #     n -=i
        # return i    
        
        # O(log n) Time, using n(n+1)/2 to sum all elements to n
        lower = 1
        upper = n
        curr = 0
        res = 0
        while lower <= upper:
            mid = lower + (upper-lower)//2
            curr = (mid/2)*(mid+1)
            if curr > n:
                upper = mid - 1
            else:
                lower = mid + 1
                res = max(mid, res)
        return res