class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        freq = set()
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
        
        def FindCycle(root):

            if vis[root] == 1:
                return True
            
            if vis[root] == 2:
                return False
            
            for nei in graph[root]:
                freq.add(nei)
                if FindCycle(nei):
                    return -1
            
            vis[root] = 2
            return False
            
        
        vis = [0] * n
        for i in range(n):
            if vis[i] == 0:
                if FindCycle(i):
                    return -1
        
        store = 0
        count = 0
        
        for i in range(n):
            if i not in freq:
                count += 1
                store = i

        if count == 1:
            return store
        else:
            return -1


        

        

        
