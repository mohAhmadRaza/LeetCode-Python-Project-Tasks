class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        
        return nums


#--------------------------------------------------2ND SOLUTION----------------------------------------
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if not nums:
            return

        left, right = 0, 1

        while left < right and right < len(nums):
            if nums[left] != 0:
                left = left + 1
                right = right + 1

            elif nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left = left + 1
                right = right + 1
            else:
                right = right + 1
        

