class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        for num in nums:
            curr = max(prev2 + num, prev1)
            prev2 = prev1
            prev1 = curr
        return max(prev1, prev2)