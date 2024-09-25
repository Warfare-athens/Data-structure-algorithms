"""     https://leetcode.com/problems/find-pivot-index/solutions/5831678/python-beats-95/      """


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total  , left_sum = sum(nums) , 0

        for i in range(len(nums)) :
            right_sum = total - nums[i] - left_sum 
            if right_sum == left_sum:
                return i 
            left_sum += nums[i]
        return -1
