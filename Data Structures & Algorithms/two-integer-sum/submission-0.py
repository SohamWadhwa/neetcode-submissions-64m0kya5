class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        prefix = {}

        for i in range(n):
            rem = target - nums[i]

            if rem in prefix:
                return [prefix[rem], i]
            
            prefix[nums[i]] = i
        
        return []