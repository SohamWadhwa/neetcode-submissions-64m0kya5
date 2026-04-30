class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        ahead = [0] * (n + 1)

        for idx in range(n - 1, -1, -1):
            curr = [0] * (n + 1)
            for prevIdx in range(idx - 1, -2, -1):
                notTake = ahead[prevIdx + 1]
                take = 0
                if prevIdx == -1 or nums[idx] > nums[prevIdx]:
                    take = 1 + ahead[idx + 1]

                curr[prevIdx + 1] = max(take, notTake)
            ahead = curr

        return ahead[0]

        # def dfs(idx, prevIdx):
        #     if dp[idx][prevIdx] != -1:
        #         return dp[idx][prevIdx]
            
        #     if idx == n:
        #         return 0
            
        #     notTake = dfs(idx + 1, prevIdx)

        #     take = 0
        #     if prevIdx == -1 or nums[idx] > nums[prevIdx]:
        #         take = 1 + dfs(idx + 1, idx)
            
        #     dp[idx][prevIdx] = max(take, notTake)
        #     return dp[idx][prevIdx]
        
        # return dfs(0, -1)