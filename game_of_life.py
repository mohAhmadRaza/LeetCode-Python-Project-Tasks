class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        newboard = []
        newboard = copy.deepcopy(board)

        cols = len(board[0])
        rows = len(board)

        for i in range(rows):
            for j in range(cols):
                lives = 0

                if i-1 >=0 and j-1 >= 0 and board[i-1][j-1] == 1:
                    lives += 1
                if i+1 <= rows-1 and j+1 <= cols-1 and board[i+1][j+1] == 1:
                    lives += 1
                if j-1 >= 0 and board[i][j-1] == 1:
                    lives += 1
                if  j+1 <= cols-1 and board[i][j+1] == 1:
                    lives += 1
                if  i+1 <= rows-1 and board[i+1][j] == 1:
                    lives += 1
                if  i-1 >= 0 and board[i-1][j] == 1:
                    lives += 1
                if i-1 >= 0 and j+1 <= cols-1 and board[i-1][j+1] == 1:
                    lives += 1
                if i+1 <= rows-1 and j-1 >= 0 and board[i+1][j-1] == 1:
                    lives += 1
                

                if board[i][j] == 1 and lives < 2:
                    newboard[i][j] = 0
                
                if board[i][j] == 1 and lives >=2 and lives <= 3:
                    continue
                
                if board[i][j] == 1 and lives > 3:
                    newboard[i][j] = 0
                
                if board[i][j] == 0 and lives == 3:
                    newboard[i][j] = 1
        

        for i in range(rows):
            for j in range(cols):
                board[i][j] = newboard[i][j]

        

                



        
        
