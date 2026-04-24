class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in times:
            graph[u-1].append([v-1, w])
        
        dist = [10**8] * n
        dist[k - 1] = 0
        q = [(0, k - 1)]

        while q:
            time, node = heapq.heappop(q)

            # if time > dist[node]:
            #     continue
            
            for nei, w in graph[node]:
                if dist[node] + w < dist[nei]:
                    dist[nei] = dist[node] + w
                    heapq.heappush(q, (time + w, nei))
        
        if max(dist) != 10**8:
            return max(dist)

        return -1