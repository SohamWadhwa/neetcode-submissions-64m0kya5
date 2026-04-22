class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        numOfIslands = 0

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(x, y):
            # if x < 0 or y < 0 or x >= m or y >= n:
            #     return
            
            grid[x][y] = '0'
            for dx, dy in dirs:
                X = x + dx
                Y = y + dy
                if 0 <= X < m and 0 <= Y < n and grid[X][Y] == '1':
                    dfs(X, Y)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    numOfIslands += 1
        
        return numOfIslands
            