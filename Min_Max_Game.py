class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        length = len(nums)
        while length > 1:
            newArray = [0] * (length // 2)

            for i in range(length // 2):
                if i % 2 == 0:
                    newArray[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    newArray[i] = max(nums[2 * i], nums[2 * i + 1])
            
            length = len(newArray)
            nums = newArray
        
        return nums[0]
