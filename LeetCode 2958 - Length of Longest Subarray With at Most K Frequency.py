"""     https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/solutions/5742444/python-beats-95/     """



class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dict = defaultdict(int)
        l = 0
        res = 0
        
        for r in range(len(nums)):
            dict[nums[r]] += 1
            
            while dict[nums[r]] > k:
                dict[nums[l]] -= 1
                l+=1
            res = max(res, r - l + 1)
        return res
