class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l = len(s)
        m = len(t)

        p = []
        q = []


        for i in range(0, l):
            if s[i] == "#":
                if p:
                    p.pop()
            else:
                if s[i] != "#":
                    p.append(s[i])
        
        for i in range(0, m):  
            if t[i] == "#":
                if q:
                    q.pop()
            
            else:
                if t[i] != "#":
                    q.append(t[i])
        
        return p == q
            
                
