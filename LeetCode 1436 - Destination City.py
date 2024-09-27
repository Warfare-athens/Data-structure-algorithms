"""     https://leetcode.com/problems/destination-city/solutions/5839529/python-beats-95/     """


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        count = set()

        for p in paths:
            count.add(p[0])
        for p in paths:
            if p[1] not in count:
                return p[1]
