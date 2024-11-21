class Solution:
    def findComplement(self, num: int) -> int:

        return num ^ ((1<<num.bit_length()) - 1)




class Solution:
    def findComplement(self, num: int) -> int:

        Binary = bin(num)[2:]
        XORwith = int('1'*len(Binary), 2)
        return num ^ XORwith
