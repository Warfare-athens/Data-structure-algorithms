https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        going_down  = False
        current_row = 0
        res = ['']*numRows

        for i in s:
            res[current_row] += i
            
            if current_row == 0 or current_row == numRows-1:
                going_down = not going_down
            if going_down:
                current_row += 1
            else:
                current_row -= 1
            
        return ''.join(res)


