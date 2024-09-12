"""     https://leetcode.com/problems/count-the-number-of-consistent-strings/solutions/5774760/python-beats-95/     """


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = len(words)

        for i in words:
            for j in i:
                if j not in allowed:
                    res -= 1
                    break
        return res
