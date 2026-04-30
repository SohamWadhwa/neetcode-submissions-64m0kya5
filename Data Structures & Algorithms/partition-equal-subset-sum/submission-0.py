class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
            
        n = len(nums)

        cache = {}
        def dfs(idx, target):
            if target == 0:
                return True
            if idx == n or target < 0:
                return False
            if (idx, target) in cache:
                return cache[(idx, target)]

            cache[(idx, target)] = (
                dfs(idx + 1, target - nums[idx])
                or 
                dfs(idx + 1, target)
            )
            return cache[(idx, target)]
        
        return dfs(0, total // 2)