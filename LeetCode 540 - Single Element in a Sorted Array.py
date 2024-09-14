"""     https://leetcode.com/problems/single-element-in-a-sorted-array/solutions/5784819/python-beats-95/     """



class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # If the array contains only one element
        if len(nums) == 1:
            return nums[0]

        # Check if the first or last element is the single non-duplicate
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-2] != nums[-1]:
            return nums[-1]

        while l <= r:
            mid = (l + r) // 2

            # Ensure that mid is within bounds and check for the non-duplicate element
            if mid > 0 and mid < len(nums) - 1 and nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]

            # Binary search: Adjust left or right depending on the pairing pattern
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                l = mid + 1
            else:
                r = mid - 1

        return nums[l]
