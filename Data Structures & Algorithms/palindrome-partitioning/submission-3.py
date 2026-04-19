class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for i in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
        
        res = []

        def dfs(idx, path):
            if idx == n:
                res.append(path.copy())
                return

            for i in range(idx, len(s)):
                if dp[idx][i]:
                    path.append(s[idx:i+ 1])
                    dfs(i + 1, path)
                    path.pop()
        
        dfs(0, [])
        return res