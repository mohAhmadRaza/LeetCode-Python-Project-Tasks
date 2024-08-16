class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        s = num[::-1]

        count = num.count("0")
        remove = 0
        
        for i in range(count):
            if s[i] == "0":
                remove += 1
            elif s[i] != "0":
                break
                
        if remove != 0:
            remove = len(num) - remove
            return num[:remove]
        else:
            return num

Method 2:
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')

