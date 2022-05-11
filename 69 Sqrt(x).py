# Binary Search
class Solution:
    def mySqrt(self, num: int) -> int:
        if num is 1:
            return 1
        lower = 0
        upper = num / 2
        while lower <= upper:
            mid = int(lower + (upper - lower) / 2)
            curr = mid * mid
            if curr == num:
                return mid
            if curr < num:
                lower = mid + 1
            else:
                upper = mid - 1
        return int(min(lower, upper))
