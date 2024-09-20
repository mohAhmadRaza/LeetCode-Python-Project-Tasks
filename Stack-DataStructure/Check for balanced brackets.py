stack = []

dic = {"[": "]", "(": ")", "{": "}"}

for i in s:
    if i in dic:  # Check if the character is an opening bracket
        stack.append(i)
    elif i in dic.values():  # Check if the character is a closing bracket
        if stack and dic[stack[-1]] == i:  # Check if stack is not empty and matches the last opened bracket
            stack.pop()
        else:
            print("Not Balanced")
            break
else:
    if not stack:
        print("Balanced")
    else:
        print("Not Balanced")
