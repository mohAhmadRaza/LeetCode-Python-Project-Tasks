class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i

        for a, b in operations:
            nums[d[a]] = b
            d[b] = d[a]
        
        return nums
