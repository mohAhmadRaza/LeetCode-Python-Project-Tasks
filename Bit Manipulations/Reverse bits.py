class Solution:
    def reverseBits(self, n: int) -> int:
        
        Binary = bin(n)[2:]
        Binary_Length = len(Binary)
        Complete_Binary = '0' * (32 - len(Binary)) + Binary

        return int(Complete_Binary[::-1], 2)

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):

            result = (result << 1) | (n & 1)
            n >>= 1
        
        return result

