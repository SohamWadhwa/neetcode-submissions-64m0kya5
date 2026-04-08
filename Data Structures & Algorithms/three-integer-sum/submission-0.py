class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    triplet = [nums[i], nums[j], nums[k]]
                    res.append(triplet)

                    while j < k and nums[j] == triplet[1]:
                        j += 1
                    while j < k and nums[k] == triplet[2]:
                        k -= 1
        return res
