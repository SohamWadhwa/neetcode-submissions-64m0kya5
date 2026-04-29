class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev1, prev2 = cost[0], cost[1]
        
        for i in range(2, n):
            curr = min(prev1 + cost[i], prev2 + cost[i])
            prev1 = prev2
            prev2 = curr
       
        return min(prev1, prev2)