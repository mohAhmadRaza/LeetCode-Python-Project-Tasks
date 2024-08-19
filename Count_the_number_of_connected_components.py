class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def DFS(currNode, vis):
            totalNodes = []
            stack = [currNode]
            vis[currNode] = True

            while stack:
                node = stack.pop()
                totalNodes.append(node)

                for nei in graph[node]:
                    if not vis[nei]:
                        vis[nei] = True
                        stack.append(nei)
                
            size = len(totalNodes)
            for node in totalNodes:
                if len(graph[node]) != size - 1:
                    return False
            
            return True
        
        vis = [False] * n
        count = 0
        for node in range(n):
            if not vis[node]:
                if len(graph[node]) == 0:
                    count += 1
                else:
                    if DFS(node, vis) == True:
                        count += 1
        
        return count




            
                
