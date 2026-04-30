class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        n = len(nums)

        dp = [[False] * ((total//2) + 1) for _ in range(n + 1)]
        for idx in range(n + 1):
            dp[idx][0] = True

        for idx in range(n - 1, -1, -1):
            for t in range((total//2) + 1):
                dp[idx][t] = (
                    dp[idx + 1][t - nums[idx]]
                    or 
                    dp[idx + 1][t]
                )

        return dp[0][total//2]

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