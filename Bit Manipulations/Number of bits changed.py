class Solution:
    def minChanges(self, n: int, k: int) -> int:
        # if (n ^ ((1<<n.bit_length())-1)) & k != 0:
        #     return -1
        
        if n|k != n:
            return -1

        XOR = n ^ k
        count = 0

        while XOR != 0:
            XOR = XOR & (XOR-1)
            count += 1
        
        return count
