"""     https://leetcode.com/problems/isomorphic-strings/solutions/5782113/python-beats-95/     """     


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            if (s[i] not in s_to_t) and (t[i] not in t_to_s):
                s_to_t[s[i]] = t[i]
                t_to_s[t[i]] = s[i]
            elif (s[i] in s_to_t and s_to_t[s[i]] != t[i]) or (t[i] in t_to_s and t_to_s[t[i]] != s[i]):
                return False

        return True
