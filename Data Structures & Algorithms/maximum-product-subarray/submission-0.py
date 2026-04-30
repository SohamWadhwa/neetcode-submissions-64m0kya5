class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1

        for num in nums:
            if num == 0:
                currMin, currMax = 1, 1
            tmp = currMax * num
            currMax = max(currMin * num, currMax * num, num)
            currMin = min(currMin * num, tmp, num)
            res = max(res, currMax)
        return res