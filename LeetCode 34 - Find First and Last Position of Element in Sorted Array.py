"""      https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/5799049/python-beats-95-binary-search/     """


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums , target , True )
        right = self.binarySearch(nums , target , False )
        return [left , right]

    def binarySearch(self , nums , target , leftBias):
        l , r = 0 , len(nums)-1
        i = -1

        while l <= r :
            mid = (l+r) // 2

            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                i = mid
                if leftBias == True:
                    r = mid - 1
                else :
                    l = mid + 1
        return i
