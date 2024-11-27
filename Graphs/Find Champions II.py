class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        in_degree = [0] * n

        for u, v in edges:
            in_degree[v] += 1
        
        champions = [i for i in range(n) if in_degree[i] == 0]

        if len(champions) > 1 or len(champions) == 0:
            return -1
        
        return champions[0]
