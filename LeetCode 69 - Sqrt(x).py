"""     https://leetcode.com/problems/sqrtx/solutions/5766393/python-beats-95/      """


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l <= r:
            mid = (l + r) // 2

            if mid**2 > x:
                r = mid - 1
            elif mid**2 < x:
                l = mid + 1
            else:
                return mid
                
        return r
