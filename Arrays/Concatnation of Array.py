class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        newNums = [0] * (2*n)

        for i in range(2*n):
            newNums[i] = nums[i%n]

        
        return newNums
