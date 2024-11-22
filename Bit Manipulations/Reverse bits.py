class Solution:
    def reverseBits(self, n: int) -> int:
        
        Binary = bin(n)[2:]
        Binary_Length = len(Binary)
        Complete_Binary = '0' * (32 - len(Binary)) + Binary

        return int(Complete_Binary[::-1], 2)
