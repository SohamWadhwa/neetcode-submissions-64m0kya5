class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        ahead = [0] * (n + 1) 
        for j in range(n + 1):
            ahead[j] = n - j
        
        for i in range(m - 1, -1, -1):
            curr = [0] * (n + 1)
            curr[n] = m - i
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    curr[j] = ahead[j + 1]
                else:
                    curr[j] = 1 + min(
                        curr[j + 1],
                        ahead[j],
                        ahead[j + 1]
                    )
            ahead = curr
        return ahead[0]