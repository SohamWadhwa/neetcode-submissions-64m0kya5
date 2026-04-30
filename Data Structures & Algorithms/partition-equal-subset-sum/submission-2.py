class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        n = len(nums)

        ahead = [False] * ((total//2) + 1)
        ahead[0] = True

        for idx in range(n - 1, -1, -1):
            curr = [False] * ((total//2) + 1)
            curr[0] = True
            for t in range((total//2) + 1):
                take = False
                if t >= nums[idx]:
                    take = ahead[t - nums[idx]]

                not_take = ahead[t]

                curr[t] = take or not_take
            ahead = curr

        return ahead[total//2]

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