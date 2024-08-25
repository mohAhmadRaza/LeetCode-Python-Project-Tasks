class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        seen = set()
        repeated = set()

        for i in range(len(s) -9):
            currString = s[i:i+10]

            if currString in seen:
                repeated.add(currString)
            else:
                seen.add(currString)
        
        return list(repeated)

Method 2:
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = []
        seen = set()

        left = 0
        for right in range(10, len(s)):
            currString = s[left:right]
            if currString in seen and currString not in result:
                result.append(currString)
            
            left += 1
        
        return result
