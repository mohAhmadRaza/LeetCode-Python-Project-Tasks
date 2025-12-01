class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        if len(height) < 0:
            return 0
        

        maxWater = 0
        left, right = 0, len(height) - 1

        while left < right:
            a, b = height[left], height[right]

            h = min(a, b)
            w = right - left
            maxWater = max(maxWater, h*w)

            if a < b:
                left = left + 1
            else:
                right = right - 1
        return maxWater

