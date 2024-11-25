class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for i in range(0, 32):
            countOnes, countZeros = 0, 0
            temp = 1<<i
            for num in nums:

                if num & temp == 0:
                    countZeros += 1
                elif num & temp == temp:
                    countOnes += 1
            
            if countOnes % 3 == 1:
                result = result | temp
        
        if result >= 2**31:
            result -= 2**32
            
        return result


