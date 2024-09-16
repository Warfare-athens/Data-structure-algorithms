"""     https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/5794048/python-beats-95-binary-search/     """


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums)-1

        while l<=r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid
            #  left side
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1 
                else:
                    r = mid - 1
            #  right side
            else: 
                if target < nums[mid] or target > nums[r] :
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
