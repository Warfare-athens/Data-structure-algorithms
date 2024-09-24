"""     https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/1400758137/      """


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []

        for i in range( len(nums) ):
            indx = abs(nums[i]) - 1
            nums[indx] = -1 * abs(nums[indx])

        for i , j in enumerate(nums):
            if j > 0:
                res.append((i+1))
        return res  
