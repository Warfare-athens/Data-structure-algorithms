 """ leetcode - https://leetcode.com/problems/simplify-path/solutions/5722255/python-beats-95-stack/ """  


class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []

        for i in path:
            if  i == '..':
                if stack:
                    stack.pop()
            elif i == '.' or i == '':
                continue
            else:
                stack.append(i)
        return '/'+'/'.join(stack)
