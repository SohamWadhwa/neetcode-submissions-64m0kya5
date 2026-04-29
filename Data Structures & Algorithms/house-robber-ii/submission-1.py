class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev1, prev2 = 0, 0
        for num in nums[:len(nums) - 1]:
            curr = max(prev2 + num, prev1)
            prev2 = prev1
            prev1 = curr
        
        res1 = max(prev1, prev2)

        prev1, prev2 = 0, 0
        for num in nums[1:]:
            curr = max(prev2 + num, prev1)
            prev2 = prev1
            prev1 = curr
        
        res2 = max(prev1, prev2)

        return max(res1, res2)