class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            tmp = 1
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n:
                    if matrix[i][j] < matrix[x][y]:
                        tmp = max(tmp, 1 + dfs(x, y))
            cache[(i, j)] = tmp
            return tmp
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res