class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max, right_max = [0] * n, [0] * n
        left_max[0], right_max[n - 1] = height[0], height[n - 1]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        for j in range(n - 2, -1, -1):
            right_max[j] = max(right_max[j + 1], height[j])
        
        max_rain_water = 0
        for i in range(n):
            curr_rain_water = min(left_max[i], right_max[i]) - height[i]
            max_rain_water += curr_rain_water
        return max_rain_water