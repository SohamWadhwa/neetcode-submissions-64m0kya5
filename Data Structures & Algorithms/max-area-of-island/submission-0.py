class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(x, y):
            grid[x][y] = 0
            currAr = 1
            for dx, dy in dirs:
                X = x + dx
                Y = y + dy
                if 0 <= X < m and 0 <= Y < n and grid[X][Y] == 1:
                    currAr += dfs(X, Y)
            return currAr
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res
                    