"""     https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/solutions/5745940/python-beats-95/     """


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        max_element = max(nums)
        max_count = 0 
        l = 0

        for r in range(len(nums)):
            if nums[r] == max_element:
                max_count+= 1
                
            while max_count > k or ( l<=r and max_count == k and nums[l] != max_element ):
                if nums[l] == max_element:
                    max_count -= 1
                l+=1
            if max_count == k :
                res += l + 1
        return res
