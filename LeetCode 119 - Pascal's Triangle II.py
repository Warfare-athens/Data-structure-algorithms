"""     https://leetcode.com/problems/pascals-triangle-ii/solutions/5835806/python-beats-95/     """


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        res = [1]

        for i in range(rowIndex):
            temp_row = [0] * (len(res)+1)
            for j in range(len(res)):
                temp_row[j] += res[j]
                temp_row[j+1] += res[j]
            res = temp_row 
        return res
