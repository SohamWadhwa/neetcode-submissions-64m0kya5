class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def solve(idx, target, ds):
            if target == 0:
                res.append(ds.copy())
                return
            if target < 0:
                return

            for i in range(idx, len(nums)):
                ds.append(nums[i])
                solve(i, target - nums[i], ds)
                ds.pop()
        solve(0, target, [])
        return res