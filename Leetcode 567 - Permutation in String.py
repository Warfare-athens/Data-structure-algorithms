class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L, l = len(s1)-1, 0
        cnt1, cnt2 = Counter(s1), Counter(s2[:L])

        for r, c in enumerate(s2[L:]):
            cnt2[c] += 1
            if cnt1 == cnt2: return True
            cnt2[s2[l]] -= 1
            l += 1

        return False
