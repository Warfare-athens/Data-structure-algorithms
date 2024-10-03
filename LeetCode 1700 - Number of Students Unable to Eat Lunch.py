"""     https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/solutions/5864072/python-beats-95/     """


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)
        res = len(students)
        
        for s in sandwiches:
            if s in count and count[s] > 0:
                res -= 1
                count[s] -= 1
            else:
                return res
        return 0
