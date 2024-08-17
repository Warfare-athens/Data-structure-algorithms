class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        nums.sort(key=lambda x:( freq[x] , -x ) )

        return nums
