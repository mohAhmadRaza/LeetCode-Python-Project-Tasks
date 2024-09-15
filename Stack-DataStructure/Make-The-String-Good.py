class Solution:
    def makeGood(self, s: str) -> str:
        if not s:
            return s
        
        stack, length, i, currLetter = [], len(s), 0, ""

        while i <= length-1:
            if s[i].isupper():
                currLetter = s[i].lower()
                if stack and currLetter == stack[-1]:
                    stack.pop()
                else:
                    stack.append(s[i])
            elif s[i].islower():
                currLetter = s[i].upper()
                if stack and currLetter == stack[-1]:
                    stack.pop()
                else:
                    stack.append(s[i])
            
            i += 1
            
        return ''.join(stack)


Method ## 2
class Solution:
    def makeGood(self, s: str) -> str:
        if not s:
            return s
        
        stack = []

        for char in s:
            if stack and char != stack[-1] and char.lower() == stack[-1].lower():
                stack.pop()
            else:
                stack.append(char)
            
        return ''.join(stack)
