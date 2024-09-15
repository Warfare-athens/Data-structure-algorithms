"""      https://leetcode.com/problems/koko-eating-bananas/solutions/5790086/python-beats-95/     """

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        res = max(piles)

        while l <= r:
            mid = (l+r) // 2
            curr_sum = 0

            for i in piles:
                curr_sum += math.ceil(i/mid)
            
            if curr_sum <= h :
                res = min( res , mid)
                r = mid-1
            else:
                l = mid +1
        return res
