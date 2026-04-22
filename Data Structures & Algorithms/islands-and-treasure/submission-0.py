class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                X, Y = x + dx, y + dy
                if 0 <= X < m and 0 <= Y < n and grid[X][Y] == 2**31 - 1:
                    grid[X][Y] = grid[x][y] + 1
                    q.append((X, Y))
                    
                