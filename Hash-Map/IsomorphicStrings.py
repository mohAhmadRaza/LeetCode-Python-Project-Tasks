class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(set(s)) != len(set(t)):
            return False
        
        FreqS, FreqT, n = {}, {}, len(s)

        for i in range(n):
            if s[i] not in FreqS:
                FreqS[s[i]] = i
            
            if t[i] not in FreqT:
                FreqT[t[i]] = i

            if FreqS[s[i]] != FreqT[t[i]]:
                return False
        return True


******************************************************* SOLUTION : 02 ****************************************************************

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(set(s)) != len(set(t)):
            return False
        FreqS, FreqT = Counter(s), Counter(t)
                n = len(s)
        
                for i in range(n):
                    if FreqS[s[i]] != FreqT[t[i]]:
                        return False
        
                    FreqS[s[i]] -= 1
                    FreqT[t[i]] -= 1
                
                return True
        
