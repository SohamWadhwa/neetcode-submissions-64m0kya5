class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return dp[amount] if dp[amount] != float('inf') else -1
        

        # def solve(amount):    
        #     if amount == 0:
        #         return 0
        #     if amount < 0:
        #         return float('inf')
        #     if dp[amount] != -1:
        #         return dp[amount]
            
        #     res = float('inf')
        #     for coin in coins:
        #         res = min(res, 1 + solve(amount - coin))

        #     dp[amount] = res
        #     return res
        
        # res = solve(amount)
        # return res if res != float('inf') else -1