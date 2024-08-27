class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        l = 0
        
        for r in range(len(s)):
            if s[r] == ' ' or r == len(s)-1:
                temp_l , temp_r = l , r-1

                if r == len(s)-1:
                    temp_r = r

                while temp_l < temp_r:
                    s[temp_l] , s[temp_r] = s[temp_r] , s[temp_l]
                    temp_l += 1
                    temp_r -= 1
                l = r+1

        return ''.join(s)
