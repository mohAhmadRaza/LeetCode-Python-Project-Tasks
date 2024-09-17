class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        matrix, arr = [], []
        totalElements = len(mat[0] * len(mat))

        if totalElements < r * c:
            return mat

        if totalElements > r * c:
            return mat

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if len(matrix) < c:
                    matrix.append(mat[i][j])
                
                if len(matrix) >= c:
                    arr.append(matrix)
                    matrix = []
        
        return arr
