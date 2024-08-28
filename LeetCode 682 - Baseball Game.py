class Solution:
    def calPoints(self, operations: List[str]) -> int:  
        stack = []

        for i in operations:
          
            if i == "D" and len(stack) >= 2:
                stack.append( stack[-1]*2 )
              
            elif i == "C" and len(stack) >= 1:
                stack.pop()
              
            elif i == "+" and len(stack) >= 1:
                stack.append( stack[-1] + stack[-2] )
            
            else:
                stack.append(int(i))

        return sum(stack)
