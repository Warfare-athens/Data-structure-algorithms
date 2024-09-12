"""     https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/solutions/5776147/python-beats-95-binary-search/     """



class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l , r = max(weights) , sum(weights)

        def capacity(mid) :
            ship , curr_cap = 1 , mid

            for i in weights:
                if curr_cap - i < 0:
                    ship += 1
                    curr_cap = mid
                curr_cap -= i
            return ship <= days

        mid = (l+r) // 2
        res = r
        while l<=r :
            mid = (l+r) // 2
            if capacity(mid) :
                res = min( res , mid )
                r = mid - 1
            else:
                l = mid + 1
        return res


"""
- capacity function checks that if the mid is satisfies the capacity within the given days
- while loop runs and checks all the capacity btw. l to r
- then res contains the minimum capacity 
"""
