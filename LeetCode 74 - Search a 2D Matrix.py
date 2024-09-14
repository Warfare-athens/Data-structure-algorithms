"""     https://leetcode.com/problems/search-a-2d-matrix/solutions/5786177/python-beats-95/     """


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows , cols = len(matrix) , len(matrix[0])
        top , bottom = 0 , rows-1
        curr_row = (top + bottom) // 2

        while top <= bottom:        
            curr_row = (top + bottom) // 2
            if matrix[curr_row][-1] < target:
                top = curr_row + 1
            elif matrix[curr_row][0] > target:
                bottom = curr_row - 1
            else:
                break
        
        if not (top <= bottom):
            return False

        l , r = 0 , cols-1
        
        while l <= r:
            mid = (l+r) // 2
            if matrix[curr_row][mid] > target:
                r = mid -1
            elif matrix[curr_row][mid] < target:
                l = mid +1
            else :
                return True
        
        return False
