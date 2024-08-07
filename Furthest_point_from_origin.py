class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        moves = list(moves)
        Left = moves.count('L')
        right = moves.count('R')
        blanks = moves.count('_')

        if Left >= right:
            return (Left + blanks) - right
        else:
            return (right + blanks) - Left
