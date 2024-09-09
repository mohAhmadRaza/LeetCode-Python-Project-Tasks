class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1 = f'{num1:04}'
        num2 = f'{num2:04}'
        num3 = f'{num3:04}'
        
        string = ""
        for i in range(4):
            string += min(num1[i], num2[i], num3[i])
        
        return int(string)
