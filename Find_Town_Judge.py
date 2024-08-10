class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        
        trust_count = [0] * (n+1)
        trust_by_count = [0] * (n+1)

        for a, b in trust:
            trust_count[a] += 1
            trust_by_count[b] += 1
        
        for i in range(1, n+1):
            if trust_count[i] == 0 and trust_by_count[i] == n - 1:
                return i
        
        return -1

        
         
            
        
