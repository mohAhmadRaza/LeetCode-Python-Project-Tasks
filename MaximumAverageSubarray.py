class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum = sum(nums[:k])
        windowMaximum = windowSum

        for i in range(k, len(nums)):
            windowSum += nums[i] - nums[i-k]
            windowMaximum = max(windowMaximum, windowSum)
        
        return windowMaximum / k
