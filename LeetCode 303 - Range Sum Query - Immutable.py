"""      https://leetcode.com/problems/range-sum-query-immutable/solutions/5835082/python-beats-95/      """


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = []
        curr = 0
        for i in nums:
            curr += i
            self.prefix.append(curr)

    def sumRange(self, left: int, right: int) -> int:
        r = self.prefix[right] 
        l = self.prefix[left - 1] if left>0 else 0
        return r-l
