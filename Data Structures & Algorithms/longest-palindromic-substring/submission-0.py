class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        start, end = 0, 0
        
        def expandFromMid(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        
        for i in range(n):
            len1, len2 = expandFromMid(i, i), expandFromMid(i, i + 1)
            lenMax = max(len1, len2)

            if lenMax > end - start:
                start = i - ((lenMax - 1) // 2)
                end = i + (lenMax // 2)
        
        return s[start:end + 1]