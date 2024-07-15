class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directories = path.split("/")
        print(directories)
        for i in directories:
            if i == "." or not i:
                continue
            elif i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return '/' + '/'.join(stack)
