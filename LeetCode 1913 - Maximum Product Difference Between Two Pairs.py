"""     https://leetcode.com/problems/maximum-product-difference-between-two-pairs/solutions/5852939/python-beats-95/     """


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min1 = min2 = float('inf')
        max1 = max2 = 0

        for n in nums:
            if n > max2:
                if n > max1:
                    max1 , max2 = n , max1
                else:     ## n is greater than m2 but not greater than m1
                    max2 = n
            if n < min2:
                if n < min1:
                    min1 , min2 = n , min1
                else:     ## n is smaller than m2 but not smaller than m1
                    min2 = n
        return (max1 * max2) - (min1 * min2)
