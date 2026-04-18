class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def solve(idx, ds):
            nonlocal res
            if idx == len(nums):
                res.append(ds.copy())
                return
            
            ds.append(nums[idx])
            solve(idx + 1, ds)
            
            ds.pop()
            solve(idx + 1, ds)

        solve(0, [])

        return res