class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        s = s.replace('-', '')
        s = s.upper()

        import textwrap

        chunk = textwrap.wrap(s[::-1], k)

        string = '-'.join(chunk)

        return string[::-1]

############################################# Method : 2 #########################################

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:  
        
        s = s.replace('-', '')
        s = s.upper()
        head = len(s) % k
        grouping = []

        if head > 0:
            grouping.append(s[:head])
        
        for index in range(head, len(s), k):
            grouping.append(s[index: index+k])
        
        return '-'.join(grouping)

                
