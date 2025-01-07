class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        count = 0

        freq = defaultdict(int)
        for x, y in coordinates:
            for a in range(k+1):

                b = k-a
                xPrime = x^a
                yPrime = y^b

                count += freq[(xPrime, yPrime)]
            
            freq[(x, y)] += 1
        
        return count
