"""     https://leetcode.com/problems/majority-element/solutions/5804786/python-beats-95/     """


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
            
        return res        
