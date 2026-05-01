class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        moves = m + n - 2
        pick = min(m - 1, n - 1)
        res = 1

        for i in range(1, pick + 1):
            res = res * (moves - pick + i) // i

        return res