"""     https://leetcode.com/problems/squares-of-a-sorted-array/solutions/5760306/python-beats-95-binary-search/     """


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l , r = 0 , len(nums)-1
        res = []
        while l <= r:

            if nums[l]*nums[l] > nums[r]*nums[r] :
                res.append( nums[l]*nums[l] ) 
                l += 1
            else :
                res.append( nums[r]*nums[r] )
                r -= 1
        return res[::-1]
