"""     https://leetcode.com/problems/binary-search/solutions/5754770/python-beats-95-binary-search/     """


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums)-1

        while l<=r:
            m = round( (l+r) /2 )
            
            if nums[m] > target:
                r = m-1
            elif  nums[m] < target:
                l = m+1
            else:
                return m
        return -1
