class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        arr1 = []
        arr1.append(nums[0])

        arr2 = []
        arr2.append(nums[1])

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            elif arr1[-1] < arr2[-1]:
                arr2.append(nums[i])
        
        arr1.extend(arr2)
        return arr1
