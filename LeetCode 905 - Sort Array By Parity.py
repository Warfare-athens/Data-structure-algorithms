class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []

        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        return even + odd



-----------------------------------  OR  ------------------------------------------



class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        l = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 0:
            nums[l] , nums[r] = nums[r] , nums[l] 
            l+=1
        return nums


