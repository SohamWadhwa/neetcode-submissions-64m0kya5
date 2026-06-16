class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            ones = 0
            for j in range(32):
                if i & (1 << j):
                    ones += 1
            res.append(ones)
        return res