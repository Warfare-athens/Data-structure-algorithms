"""     https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/solutions/5855335/python-beats-95/      """


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        chars = Counter(chars)
        
        for i in words:
            cur_word = defaultdict(int)
            good = True
            
            for j in i:
                cur_word[j] += 1
                if j not in chars or cur_word[j] > chars[j] :
                    good = False
            if good:
                res += len(i)
                
        return res   
