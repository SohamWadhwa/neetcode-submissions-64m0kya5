class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1

        while numbers[l] + numbers[r] != target:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
        
        return [l + 1, r + 1]