class Solution:
    # Space O(1) and Time O(n)
    # Basically the fib problem
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 1, 1
        for i in range(2, n + 1):
            b = a + b
            a = b - a
        return b