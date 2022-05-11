# Binary Search
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num is 1:
            return True
        lower = 0
        upper = num/2
        while lower <= upper:
            mid = int(lower + (upper-lower)/2)
            curr = mid*mid
            if curr == num:
                return True
            if curr < num:
                lower = mid + 1
            else:
                upper = mid - 1
        return False