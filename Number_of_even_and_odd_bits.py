class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        string = bin(n)[2:]
        even, odd = 0, 0

        for i in range(len(string)):
            if string[-(i+1)] == '1':
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
        
        return [even, odd]
