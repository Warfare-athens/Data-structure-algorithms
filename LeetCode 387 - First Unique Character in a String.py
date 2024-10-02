"""      https://leetcode.com/problems/first-unique-character-in-a-string/solutions/5861287/python-beats-95/     """


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)

        for i in s:
            count[i] += 1

        for i , j in enumerate(s):
            if count[j] == 1:
                return i
        return -1
