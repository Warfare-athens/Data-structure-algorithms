"""     https://leetcode.com/problems/fruit-into-baskets/solutions/5746918/python-beats-95-sliding-window/     """



class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        l , total , res  = 0 , 0 , 0 

        for r in range(len(fruits)):
            count[fruits[r]] += 1
            total += 1

            while  len(count) > 2:
                count[fruits[l]] -= 1
                total -= 1
                if count[fruits[l]] == 0:
                    count.pop(fruits[l])
                l+=1
                
            res = max(res , total)

        return res
