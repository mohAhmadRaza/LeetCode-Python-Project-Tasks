class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        cols = len(board[0])
        rows = len(board)

        for i in range(rows):
            for j in range(cols):
                lives = 0

                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if x==0 and y==0:
                            continue
                        
                        r, c = i + x, j + y

                        if  0 <= r < rows and 0 <= c < cols:
                            if board[r][c] & 1:
                                lives += 1
                

                if board[i][j] & 1:                    
                    if lives == 2 or lives == 3:
                        board[i][j] |= 2

                else:
                    if lives == 3:
                        board[i][j] |= 2
                                    
        for i in range(rows):
            for j in range(cols):

                board[i][j] >>= 1
        
        
