class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # Nmber of rows
        rows = len(grid)

        # Number of columns
        cols = len(grid[0])

        # Checking if grid is less than 3*3
        if rows < 3 or cols < 3:
            return 0
        
        def isMagicSquare(grid, rowStart, colStart):
            # set to store distinct integers
            distinctElements = set()
            
            # row, column, rightDiagonal, LeftDiagonal Sum
            allSums, rightDiagonal, leftDiagonal = [], 0, 0

            for i in range(3):

                # re initialzing sums for every row and column
                rowSum, colSum = 0, 0

                for j in range(3):

                    # checking if the number is in range of 1-9
                    if grid[rowStart + i][colStart + j] < 1 or grid[rowStart + j][colStart + i] > 9:
                        return False
                    
                    # adding elements in sets to check they are unique or not
                    distinctElements.add(grid[rowStart + i][colStart + j])

                    # adding elements of one particular row, similarly for columns
                    rowSum += grid[rowStart + i][colStart + j]
                    colSum += grid[rowStart + j][colStart + i]
                
                # adding elements of right diagonal as [0][0], [1][1], [2][2]
                rightDiagonal += grid[rowStart + i][colStart + i]

                # adding elements of left diagonal
                leftDiagonal += grid[rowStart + i][colStart + 2-i]

                # appending sums af all rows and columns into list
                allSums.append(rowSum)
                allSums.append(colSum)
            
            # In the last appending the grid's right and left diagonals
            allSums.append(rightDiagonal)
            allSums.append(leftDiagonal)
            
            # checking if list contains elements of same value by converting it into set
            # and checking that elements in set are the length of 9, means they all are unique
            if len(set(allSums)) == 1 and len(distinctElements) == 9:
                return True
            
            # If not returing False
            return False
        

        count = 0

        # calling function for all the possible grids of length 3*3
        for i in range(rows-2):
            for j in range(cols-2):
                if isMagicSquare(grid, i, j):
                    count += 1
        return count
                
        

                    

            
