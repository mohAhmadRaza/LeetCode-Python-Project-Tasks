class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        n = len(s)
        arr = [0] * n
        count = 0

        for char in range(n):
            if s[char] == "(":
                stack.append(char)
            
            if stack and s[char] == ")":
                arr[stack.pop()] = 1
                arr[char] = 1

        temp, ans = 0, 0
        for i in arr:
            if i == 1:
                temp += 1
                ans = max(ans, temp)
            else:
                temp = 0
        
        return ans        
