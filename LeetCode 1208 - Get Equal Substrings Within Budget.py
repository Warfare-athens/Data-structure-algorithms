"""     https://leetcode.com/problems/get-equal-substrings-within-budget/solutions/5740595/python-beats-95-sliding-window/     """


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        curr = 0
        res = 0
        l = 0
        for r in range(len(s)):
            curr += abs(ord(s[r]) - ord(t[r]))
            
            while curr > maxCost:
                curr -= abs(ord(s[l]) - ord(t[l]))
                l+=1
            res = max(res , r-l+1)
        return res
