class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        for i in range(n):
            if sum(nums[i+1:]) == sum(nums[:i]):
                return i
        
        return -1
