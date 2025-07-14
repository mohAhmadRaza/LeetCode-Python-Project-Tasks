class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        l = len(s)

        chars = list(s[1:])
        results = [s[0]]

        for i in range(0, l-1):
            if results:
                if chars[i] == results[-1]:
                    results.pop()
            

                elif chars[i] != results[-1]:
                    results.append(chars[i])
            
            else: 
                results.append(chars[i])
        
        return "".join(results)

                
            

            




