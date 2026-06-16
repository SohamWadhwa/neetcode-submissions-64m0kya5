class Solution:
    def hammingWeight(self, n: int) -> int:
        bits_1 = 0

        for i in range(32):
            if n & (1 << i):
                bits_1 += 1
        return bits_1