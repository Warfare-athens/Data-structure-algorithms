"""     https://leetcode.com/problems/largest-3-same-digit-number-in-string/solutions/5839385/python-beats-95/     """


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ''

        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                res = max( res , num[i:i+3] )

        return res if res else '' 
