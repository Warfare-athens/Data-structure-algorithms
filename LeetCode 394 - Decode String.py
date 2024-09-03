"""  https://leetcode.com/problems/decode-string/solutions/5730296/python-beats-95-stack/  """


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i == ']':
                
                word = ''
                while stack[-1] !='[':
                    word = stack.pop() + word
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                stack.append(int(num) * word)

            else:
                stack.append(i)

        return ''.join(stack)
