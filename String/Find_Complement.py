class Solution:
    def findComplement(self, num: int) -> int:
        
        string = bin(num)[2:]
        string = string.replace('0', '2')
        string = string.replace('1', '0')
        string = string.replace('2', '1')

        string.lstrip('0')

        return int(string, 2)
