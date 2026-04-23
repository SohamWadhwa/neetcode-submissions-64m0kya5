class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        vis = [0] * numCourses
        for u, v in prerequisites:
            adj[u].append(v)
        
        def isCycle(node):
            vis[node] = 1
            for nei in adj[node]:
                if vis[nei] == 0 and isCycle(nei):
                    return True
                elif vis[nei] == 1:
                    return True
            vis[node] = 2
            return False
                    
        
        for i in range(numCourses):
            if not vis[i] and isCycle(i):
                return False
        return True