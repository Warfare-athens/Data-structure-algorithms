"""      https://leetcode.com/problems/subarray-product-less-than-k/solutions/5746693/python-beats-95-sliding-window/      """


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        count = 1
        l = 0

        for r in range(len(nums)):
            count = count*nums[r]

            while l <= r and count >= k:
                count = count // nums[l]
                l += 1
            res += r-l+1
        return res
