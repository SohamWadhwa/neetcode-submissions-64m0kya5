class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n - 1

        max_water = 0
        while left < right:
            curr_water = 0
            length = right - left
            if heights[left] < heights[right]:
                curr_water = heights[left] * length
                left += 1
            else:
                curr_water = heights[right] * length
                right -= 1
            max_water = max(max_water, curr_water)
        
        return max_water
