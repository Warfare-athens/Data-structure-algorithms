from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        int_five = 0
        int_ten = 0
        
        for i in bills:
            if i == 5:
                int_five += 1
            
            elif i == 10:
                if int_five > 0:
                    int_five -=1
                else:
                    return False
                int_ten += 1
            else:
                if int_five > 0 and int_ten > 0:
                    int_five -=1
                    int_ten -= 1
                elif int_five>2:
                    int_five -= 3
                else:
                    return False
        return True
        
print(Solution().lemonadeChange( [5,5,10,10,20] ))
