"""      https://leetcode.com/problems/successful-pairs-of-spells-and-potions/solutions/5785581/python-beats-95/     """


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()

        for s in spells:
            
            l , r = 0 , len(potions)-1
            index = len(potions)-1

            while l <= r:
                mid = (l+r) // 2
                if s*potions[mid] >= success:
                    r = mid-1
                    index = mid
                else:
                    l = mid + 1
            res.append(( len(potions) - index ))        
        return res
