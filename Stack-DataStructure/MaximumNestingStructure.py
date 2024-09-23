class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = 0
        count = 0

        for i in s:
            if i == "(":
                count += 1
            
            if i == ")":
                maxi = max(maxi, count)
                count -= 1
        
        return maxi

############################### Method #2  ###################################
class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxi = 0
        count = 0

        for i in s:
            if i == "(":
                stack.append(i)
                maxi = max(maxi, len(stack))
            
            if i == ")":
                stack.pop()
        
        return maxi
