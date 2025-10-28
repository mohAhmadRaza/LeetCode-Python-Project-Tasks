class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 0
        right = 1

        n = len(nums)
        result = []

        nums.sort()

        for i in range(n):
            if (i>0 and nums[i] == nums[i-1]):
                continue
            
            left = i+1
            right = n-1

            while (left < right):
                summation = (nums[i] + nums[left] + nums[right])

                if (summation > 0):
                    right = right - 1
                elif (summation < 0):
                    left = left+1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    left = left+1
                    right= right-1
                    while(left > 0 and left < right and nums[left] == nums[left-1]):
                        left = left+1
                    while(right < n-1 and left < right and nums[right] == nums[right + 1]):
                        right = right-1
        return result
                
                

            
