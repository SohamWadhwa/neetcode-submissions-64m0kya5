class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        cache = {}
        def dfs(idx, target):
            if (idx, target) in cache:
                return cache[(idx, target)]
            if idx == n:
                if target == 0:
                    return 1
                return 0
            res = dfs(idx + 1, target + nums[idx])
            res += dfs(idx + 1, target - nums[idx])
            cache[(idx, target)] = res
            return res

        return dfs(0, target)  
            
            