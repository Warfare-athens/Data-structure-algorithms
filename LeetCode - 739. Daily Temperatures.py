https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        
        for i , j in enumerate(temperatures):
            
            while stack and j > stack[-1][0]:
                temp_j , temp_i = stack.pop()
                res[temp_i] = i - temp_i 
                
            stack.append((j,i))
        
        return res
