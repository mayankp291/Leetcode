class Solution:
    # Space O(1) and Time O(n)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for i in range(2, n + 1):
            b = a + b
            a = b - a
        return b
