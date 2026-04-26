class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))
        
        q = deque([(0, src, 0)])
        dist = [float('inf')] * n
        dist[src] = 0

        while q:
            stops, node, cost = q.popleft()

            if stops > k:
                continue
            
            for nei, wt in graph[node]:
                if cost + wt < dist[nei] and stops <= k:
                    dist[nei] = cost + wt
                    q.append((stops + 1, nei, dist[nei]))
        
        return dist[dst] if dist[dst] != float('inf') else -1