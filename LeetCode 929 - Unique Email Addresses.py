"""     https://leetcode.com/problems/unique-email-addresses/solutions/5781031/python-beats-95/     """


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails: set[str] = set()
        for email in emails:
                
            first , last = email.split('@')
            first = first.split('+')[0]
            first = first.replace('.' , '')
            unique_emails.add(first + '@' + last)
        
        return len(unique_emails)
