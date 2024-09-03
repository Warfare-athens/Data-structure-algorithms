"""   https://leetcode.com/problems/sum-of-digits-of-string-after-convert/solutions/5730654/python-beats-95/   """


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        number = ''
        for x in s:
            number += str(ord(x) - ord('a') + 1)
        
        while k > 0:
            temp = 0
            for x in number:
                temp += int(x)  # Sum the digits of the current number
            number = str(temp)  # Convert the sum back to a string
            k -= 1
        return int(number)  # Return the final result as an integer
