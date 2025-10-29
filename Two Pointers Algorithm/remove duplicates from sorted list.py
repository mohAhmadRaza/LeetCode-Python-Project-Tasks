class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return 1

        right = 1

        total = 1
        left = 0

        while right < n:

            if nums[left] == nums[right]:
                right = right + 1
            
            elif nums[left] != nums[right]:
                total = total + 1
                if left < n-1:
                    left = left + 1
                    nums[left], nums[right] = nums[right], nums[left]
                    right = right + 1

        return total
