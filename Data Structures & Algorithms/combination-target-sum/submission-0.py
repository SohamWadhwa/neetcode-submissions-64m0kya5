class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def solve(idx, target, ds):
            nonlocal res
            if idx == len(nums):
                if not target:
                    res.append(ds.copy())
                return 

            if target < 0:
                return
            
            solve(idx + 1, target, ds)

            ds.append(nums[idx])
            solve(idx, target - nums[idx], ds)
            ds.pop()
        
        solve(0, target, [])
        return res