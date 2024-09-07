"""     https://leetcode.com/problems/minimum-time-to-make-rope-colorful/solutions/5749924/python-beats-95-two-pointer/     """


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res , l = 0 , 0

        for r in range(1 , len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    res += neededTime[l]
                    l = r
                else:
                    res += neededTime[r]
                
            else:
                l = r
        return res
