class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        negative = len([1 for x in nums if x < 0])

        for i in range(min(negative, k)):
            nums[i] = nums[i]*-1
            k -= 1
        
        if negative:
           nums.sort()

        for i in range(k):
            nums[0] = nums[0]*-1
        
        return sum(nums)

        


