class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        N = 2**n

        for i in range(N):
            tmp = []
            for j in range(n):
                if i & (1 << j):
                    tmp.append(nums[j])
            res.append(tmp)
        return res