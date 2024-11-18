class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        Perimeter = 0
        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 1:
                    if row-1 >=0:
                        if grid[row-1][col] == 0:
                            Perimeter += 1
                    elif row-1 < 0:
                        Perimeter += 1

                    if row+1 <= rows-1:
                        if grid[row+1][col] == 0:
                            Perimeter += 1
                    elif row+1 > rows-1:
                        Perimeter += 1

                    if col-1 >=0:
                        if grid[row][col-1] == 0:
                            Perimeter += 1
                    elif col-1 < 0:
                        Perimeter += 1

                    if col+1 <= cols-1: 
                        if grid[row][col+1] == 0:
                            Perimeter += 1
                    elif col+1 > cols-1:
                        Perimeter += 1
                
                else:
                    continue
        
        return Perimeter
