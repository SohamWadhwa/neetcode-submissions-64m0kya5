class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        res = 0
        def expandFromMid(l, r):
            palCnt = 0
            while l >= 0 and r < n and s[l] == s[r]:
                palCnt += 1
                l -= 1
                r += 1
            return palCnt
        
        for i in range(n):
            res += expandFromMid(i, i)
            res += expandFromMid(i, i + 1)
        
        return res