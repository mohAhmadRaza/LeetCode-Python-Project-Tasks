class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [-1] * len(nums)

        for i in range(2 * n):
            currElement = nums[i % n]
            
            while stack and nums[stack[-1]] < currElement:
                index = stack[-1]
                res[index] = currElement
                stack.pop()
            
            if i < n:
                stack.append(i)
                
        return res
        

