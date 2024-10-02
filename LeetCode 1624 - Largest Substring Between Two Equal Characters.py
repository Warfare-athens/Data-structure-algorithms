"""     https://leetcode.com/problems/largest-substring-between-two-equal-characters/solutions/5860178/python-beats-95/     """


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_count = {}
        res = -1
        
        for idx , char in enumerate(s):
            if char in char_count :
                res = max( res , (idx - char_count[char] - 1 ) )
            else:
                char_count[char] = idx
        return res
