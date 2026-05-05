class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        ahead = [0] * (n + 1)
        ahead[n] = 1
        
        for i in range(m - 1, -1, -1):
            curr = [0] * (n + 1)
            curr[n] = 1
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    curr[j] = ahead[j + 1] + ahead[j]
                else:
                    curr[j] = ahead[j]
            ahead = curr
        
        return ahead[0]