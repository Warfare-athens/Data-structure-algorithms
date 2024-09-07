"""      https://leetcode.com/problems/rearrange-array-elements-by-sign/solutions/5750490/python-beats-95-two-pointer/     """



class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i , j = 0 , 1
        res = [0]*len(nums)

        for k in range(len(nums)):
            if nums[k]  > 0:
                res[i] = nums[k]
                i = i+2
            else :
                res[j] = nums[k]
                j = j+2
        
        return res
