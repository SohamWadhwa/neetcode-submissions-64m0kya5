class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ahead = [0] * 2
        ahead2 = 0

        for idx in range(n - 1, -1, -1):
            curr = [0, 0]

            curr[1] = max(
                -prices[idx] + ahead[0],
                ahead[1] 
            )

            curr[0] = max(
                prices[idx] + ahead2,
                ahead[0]
            )

            ahead2 = ahead[1]
            ahead = curr

        return ahead[1]