class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        
        res = -1
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in dirs:
                    X, Y = x + dx, y + dy
                    if 0 <= X < m and 0 <= Y < n and grid[X][Y] == 1:
                        grid[X][Y] = 2
                        q.append((X, Y))
                        fresh -= 1
            res += 1
        return res if fresh == 0 else -1