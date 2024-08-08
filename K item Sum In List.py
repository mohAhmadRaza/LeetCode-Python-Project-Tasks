class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        L = [1]*numOnes
        if numZeros:
            L.extend([0]*numZeros)
        if numNegOnes:
            L.extend([-1]*numNegOnes)
        

        return sum(L[:k])
