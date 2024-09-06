class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        i, length = 0, len(s)

        while i < length:
            if s[i] == '*':
                stack.pop()
            else:
                stack.append(s[i])

            i += 1
        
        return ''.join(stack)
        


