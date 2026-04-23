class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        vis = set()
        def dfs(node, parent):
            vis.add(node)

            for nei in adj[node]:
                if nei != parent and nei not in vis:
                    dfs(nei, node)
        
        comps = 0
        for i in range(n):  
            if i not in vis:
                dfs(i, -1)
                comps += 1
        
        return comps