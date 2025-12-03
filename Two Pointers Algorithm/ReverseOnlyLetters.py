class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n = len(s)

        strList = list(s)
        left, right = 0, n - 1

        while left < right:

            if strList[left].isalpha() and strList[right].isalpha():
                strList[left], strList[right] = strList[right], strList[left]
                left = left + 1
                right = right - 1
            
            elif strList[left].isalpha() and not strList[right].isalpha():
                right = right - 1
            
            elif strList[right].isalpha() and not strList[left].isalpha():
                left = left + 1
            
            elif not strList[right].isalpha() and not strList[left].isalpha():
                left = left + 1
                right = right - 1
        
        return "".join(strList)
