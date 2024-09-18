class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack = []

        for i in range(len(nums)):
            if stack.count(nums[i]) < 2:
                stack.append(nums[i])
            else:
                continue
        
        for i in range(len(stack)):
            nums[i] = stack[i]
        
        return len(stack)
