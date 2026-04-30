class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [-1] * (amount + 1)

        def solve(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            if dp[amount] != -1:
                return dp[amount]
            
            res = float('inf')
            for coin in coins:
                res = min(res, 1 + solve(amount - coin))

            dp[amount] = res
            return res
        
        res = solve(amount)
        return res if res != float('inf') else -1