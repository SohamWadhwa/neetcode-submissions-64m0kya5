class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        vis = [0] * numCourses
        for u, v in prerequisites:
            adj[v].append(u)
        
        res = []
        def isCycle(node):
            vis[node] = 1
            for nei in adj[node]:
                if vis[nei] == 0 and isCycle(nei):
                    return True
                elif vis[nei] == 1:
                    return True
            vis[node] = 2
            res.append(node)
            return False
                    
        for i in range(numCourses):
            if not vis[i] and isCycle(i):
                return []
        return res[::-1]