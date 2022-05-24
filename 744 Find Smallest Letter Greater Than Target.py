class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        # initial condition
        if letters[n-1] <= target or target < letters[0]:
            return letters[0]
        lower = 0
        upper = n-1
        # binary search
        while lower <= upper:
            mid = lower + (upper-lower)//2
            curr = letters[mid]
            if target < curr:
                upper = mid - 1
            else:
                lower = mid + 1
        return letters[lower]