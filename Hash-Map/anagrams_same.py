class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashedTable1 = Counter(s)
        hashedTable2 = Counter(t)
        unique = set(s)
        unique.update(t)


        for i in unique:
            if hashedTable1[i] != hashedTable2[i]:
                return False
        
        return True
        
        
