class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i == ']':
                string = ""
                while stack[-1] != '[':
                    string = stack.pop() + string
                
                stack.pop()

                curr_num = ""
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num
                
                string = int(curr_num) * string
                stack.append(string)
                
            else:
                stack.append(i)
        
        return ''.join(stack)

                    
            
            
