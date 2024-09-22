class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l = len(original)
        if l < m * n or l > m*n:
            return []
        
        res = []
        start, end = 0, n
        for i in range(m):
            res.append(original[start : end])
            start = end
            end += n
        
        return res

                

