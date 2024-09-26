"""     https://leetcode.com/problems/monotonic-array/solutions/5835174/python-beats-95/      """


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        decresing , incresing = True , True

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                decresing = False
            elif nums[i] > nums[i+1]:
                incresing = False

        return incresing or decresing
