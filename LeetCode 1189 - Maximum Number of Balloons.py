"""      https://leetcode.com/problems/maximum-number-of-balloons/solutions/5817224/python-beats-95/     """"


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        balloon = Counter("balloon")
        res = float('inf')

        for i in balloon:
            res = min( res , count[i] // balloon[i] )

        return res      
