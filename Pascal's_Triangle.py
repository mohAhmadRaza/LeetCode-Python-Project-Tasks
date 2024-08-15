class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        array = [[1] for _ in range(numRows)]

        array[1].append(1)

        for i in range(2, numRows):
            for j in range(len(array[i-1])-1):
                array[i].append(array[i-1][j] + array[i-1][j+1])
            array[i].append(1)
        
        return array

            
