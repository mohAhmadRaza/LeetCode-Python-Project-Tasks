class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date = list(date.split('-'))
        string = []
        
        for i in date:
            i = int(i)
            string.append(bin(i)[2:])
        
        return '-'.join(string)
