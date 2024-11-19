class NumArray:

    def __init__(self, nums: List[int]):
        self.sumArray = [0] * len(nums)
        sums = 0
        for i in range(0, len(nums)):
            sums += nums[i]
            self.sumArray[i] = sums 
    
    # [-2, -2, 1, -4, -2, -3]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sumArray[right]
        elif left > 0 and right > 0:
            return self.sumArray[right] - self.sumArray[left-1]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
