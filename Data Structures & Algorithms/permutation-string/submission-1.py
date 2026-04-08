from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if m < n:
            return False
        maps1, maps2 = defaultdict(int), defaultdict(int)
        l = 0
        
        for r in range(n):
            maps1[s1[r]] += 1
            maps2[s2[r]] += 1
                
        for r in range(n, m):
            if maps1 == maps2:
                return True
            
            maps2[s2[l]] -= 1
            if maps2[s2[l]] == 0:
                del maps2[s2[l]]
            l += 1
            maps2[s2[r]] += 1
        return maps1 == maps2