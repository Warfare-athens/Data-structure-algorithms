"""     https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/solutions/5856264/python-beats-95/       """


class Solution:
    def minOperations(self, s: str) -> int:
        count_pattern1 = 0
        count_pattern2 = 0

        for i in range(len(s)):
            if i % 2:
                if s[i] == '0':
                    count_pattern1 += 1
                else:
                    count_pattern2 += 1
            
            else:
                if s[i] == '1':
                    count_pattern1 += 1
                else:
                    count_pattern2 += 1
        return min( count_pattern1 , count_pattern2  ) 
