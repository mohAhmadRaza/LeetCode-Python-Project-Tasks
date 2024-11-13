class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        groups = set(tuple(sorted(group)) for group in combinations(nums, 3))

        List = [list(group) for group in groups if sum(group) == 0]
        return List



######################################### Solution : 2 ##################################

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        temp = set()

        result = []

        for i in range(len(nums)):

            j = i + 1
            k = len(nums) - 1

            while j < k:

                tempSum = nums[i] + nums[j] + nums[k]

                if tempSum == 0:
                    temp.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                
                elif tempSum > 0:
                    k -= 1
                
                else:
                    j += 1
            
        
        result = list(temp)
        return result
