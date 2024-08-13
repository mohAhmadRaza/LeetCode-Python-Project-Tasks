class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if (len(nums) == 1 and nums[0] == 0) or not nums:
            return 0
        
        unique = set(nums)
        unique = list(unique)
        unique.sort()
        count = 0
        for i in range(len(unique)):
            if unique[i] != 0:
                count += 1

                for j in range(i+1, len(unique)):
                    unique[j] -= unique[i]
        
        return count
