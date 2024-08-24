class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        answer = 0
        
        for i in grid:
            i.sort(reverse=True)

        while len(grid[0]) > 0:
            maxi = float('-inf')
            for i in grid:
                maxi = max(maxi, i.pop(0))
            answer += maxi
        return answer
        
