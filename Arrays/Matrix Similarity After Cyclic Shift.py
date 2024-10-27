class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        matrix = copy.deepcopy(mat)
        cols, rows = len(mat[0]), len(mat)
        k = k % cols

        for j in range(rows):
            if j % 2 == 0:
                matrix[j] = matrix[j][k:] + matrix[j][:k]
            else:
                matrix[j] = matrix[j][-k:] + matrix[j][:-k]
                
        return matrix == mat
