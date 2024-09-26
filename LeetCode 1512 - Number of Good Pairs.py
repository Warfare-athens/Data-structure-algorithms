"""      https://leetcode.com/problems/number-of-good-pairs/solutions/5835649/python-beats-95/     """


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        res = 0

        for i in nums:
            if i in count:
                res += count[i]
                count[i] += 1
            else:
                count[i] = 1

        return res
