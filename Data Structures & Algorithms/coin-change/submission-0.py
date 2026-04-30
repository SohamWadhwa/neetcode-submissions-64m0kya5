class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n + 1)]

        def solve(idx, amount):
            if amount == 0:
                dp[idx][amount] = 0
                return 0
            if amount < 0 or idx == n:
                return float('inf')
            if dp[idx][amount] != -1:
                return dp[idx][amount]
            
            taken = 1 + solve(idx, amount - coins[idx])
            not_taken = solve(idx + 1, amount)

            dp[idx][amount] = min(taken, not_taken)
            return dp[idx][amount]
        
        res = solve(0, amount)
        return res if res != float('inf') else -1