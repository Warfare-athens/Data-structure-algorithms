"""   https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/solutions/5737535/python-beats-95-sliding-window/   """



class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        l = 0
        curr_sum = 0
        max_window = -1

        for r in range(len(nums)):
            curr_sum += nums[r]

            while l <= r and curr_sum > target:
                curr_sum -= nums[l]
                l+=1
            if curr_sum == target:
                max_window = max( max_window , r-l+1 )
        return -1 if max_window == -1 else len(nums) - max_window



"""   Opposite approach of solving a sum equal to a target just minus the x from then sum of [nums] then do the same approach and then return the ( len(nums) - window )   """
