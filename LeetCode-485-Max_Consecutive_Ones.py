class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            if i == 0:
                maximum = max(count, maximum)
                count = 0
        maximum = max(maximum, count)
        return maximum

