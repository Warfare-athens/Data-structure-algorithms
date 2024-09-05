"""     https://leetcode.com/problems/find-missing-observations/solutions/5741609/python-beats-95/     """


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum = mean*(m + n)
        missing_sum = total_sum - sum(rolls)
        res = [0]*n

        if missing_sum < n or missing_sum > n*6:
            return []
        
        i = 0
        while missing_sum :
            res[i] += min(6 , missing_sum - n +1)
            missing_sum -= res[i]
            n -= 1
            i+=1
            
        return res
