"""     https://leetcode.com/problems/next-greater-element-i/solutions/5830901/python-beats-95/      """


def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = { j:i for i,j in enumerate(nums1) }
        res = [-1] * len(nums1)
        stack = []

        for n in range(len(nums2)):
            curr = nums2[n]
            
            while stack and curr > stack[-1] :
                val = stack.pop()
                idx = nums[val] 
                res[idx] = curr 
            
            if curr in nums :
                stack.append(curr)
        return res
