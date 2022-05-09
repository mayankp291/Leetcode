class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = set()
        temp = ""
        for i in s:
            if i in a:
                if len(a) > len(temp):
                    temp = a
                a = set()
                a.add(i)
            else:
                a.add(i)
        return max(len(a), len(temp))