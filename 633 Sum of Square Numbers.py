# 2 sum approach of hashing O(N)
# Can be O(log n) using 2 pointers and binary search

from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c is 1 or 0:
            return True
        temp = set()
        for i in range(int(sqrt(c))+1):
            diff = c - i**2
            temp.add(i**2)
            if diff in temp:
                return True
