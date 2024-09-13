"""     https://leetcode.com/problems/pascals-triangle/solutions/5780353/python-beats-95/     """


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [ [1] ]

        for i in range( numRows-1 ):
            temp = [0] + res[-1] + [0]
            temp_res = []
            for j in range( len(temp)-1 ):
                temp_res.append( temp[j] + temp[j+1] )
            res.append( temp_res )
        
        return res
