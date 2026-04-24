from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        
        for u, v in tickets:
            heapq.heappush(graph[u], v)
        
        res = []
        
        def dfs(node):
            while graph[node]:
                nei = heapq.heappop(graph[node])
                dfs(nei)
            res.append(node)
        
        dfs("JFK")
        return res[::-1]
