class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        cache = {}
        def dfs(idx, buy):
            if idx >= n:
                return 0
            if (idx, buy) in cache:
                return cache[(idx, buy)]

            if buy:
                profit = max(
                    -prices[idx] + dfs(idx + 1, not buy),
                    dfs(idx + 1, buy)
                )
            else:
                profit = max(
                    prices[idx] + dfs(idx + 2, not buy),
                    dfs(idx + 1, buy)
                )
            cache[(idx, buy)] = profit
            return profit
        
        return dfs(0, True)