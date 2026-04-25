class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [(grid[0][0], 0, 0)]
        n = len(grid)
        vis = set([(0, 0)])
        while True:
            time, x, y = heapq.heappop(minHeap)

            if (x, y) == (n - 1, n - 1):
                return time

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                X, Y = x + dx, y + dy
                if 0 <= X < n and 0 <= Y < n and (X, Y) not in vis:
                    vis.add((X, Y))
                    if grid[X][Y] <= time:
                        heapq.heappush(minHeap, (time, X, Y))
                    else:
                        heapq.heappush(minHeap, (grid[X][Y], X, Y))
