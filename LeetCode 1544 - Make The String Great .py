class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        i = 0
        
        while i < len(s):
            if stack and stack[-1] != s[i] and stack[-1].lower() == s[i].lower():
                stack.pop()
            else:
                stack.append(s[i])
            i+=1
        return ''.join(stack)
