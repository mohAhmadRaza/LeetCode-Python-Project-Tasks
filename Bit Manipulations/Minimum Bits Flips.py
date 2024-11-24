class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        check1, count = 1, 0

        for i in range(max(a.bit_length(), b.bit_length(), c.bit_length())):
            bitA = a & check1
            bitB = b & check1
            bitC = c & check1

            if (bitA == bitB) and (bitA != bitC) and (bitA == check1):
                count += 2

            elif (bitA == bitB) and (bitA != bitC) and (bitA == 0):
                count += 1
            
            elif (bitA != bitB) and (bitC == 0):
                count += 1

            check1 <<= 1  # Shift to the next bit

        return count
