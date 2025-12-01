class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)        
        left, right = 0, n-1
        newArray = [0]*n

        for i in range(n):
            a, b = nums[left]*nums[left], nums[right]*nums[right] 
            if a < b:
                newArray[n-i-1] = b
                right = right - 1
            else:
                newArray[n-i-1] = a
                left = left + 1
        
        return newArray

