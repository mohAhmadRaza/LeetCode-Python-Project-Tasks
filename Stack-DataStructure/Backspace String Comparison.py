class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = [], []

        l1, l2 = len(s), len(t)

        for i in range(l1):
            if stack1 and s[i] == '#':
                stack1.pop()
            
            elif not stack1 and s[i] == '#':
                continue

            elif s[i] != '#':
                stack1.append(s[i])
        
        for i in range(l2):
            if stack2 and t[i] == '#':
                stack2.pop()
            
            elif not stack2 and t[i] == '#':
                continue

            else:
                stack2.append(t[i])
        
        return ''.join(stack1) == ''.join(stack2)
