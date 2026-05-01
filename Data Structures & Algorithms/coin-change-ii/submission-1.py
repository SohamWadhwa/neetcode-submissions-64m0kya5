class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        cache = {}
        def solve(idx, target):
            if target == 0:
                return 1
            if (idx, target) in cache: 
                return cache[(idx, target)]
            if idx == n:
                return 0
            
            
            res = solve(idx + 1, target)

            if target - coins[idx] >= 0:
                res += solve(idx, target - coins[idx])
            cache[(idx, target)] = res
            return res
        
        return solve(0, amount)