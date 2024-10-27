class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                a, b = bin(nums[i])[2:], bin(nums[j])[2:]

                if nums[i] > nums[j]:
                    if a.count('1') == b.count('1'):
                        nums[i], nums[j] = nums[j], nums[i]
                    else:
                        print(i)
                        return False
        
        return True
