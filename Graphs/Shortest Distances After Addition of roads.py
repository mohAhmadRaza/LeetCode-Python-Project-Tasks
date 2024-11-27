###################################### Solution Passed 772/972 Test Cases #############################

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        result = []
        graph = [[] for _ in range(n)]
        for i in range(n-1):
            graph[i].append(i+1)
        
        def DFS(node, count):
             
            if node == n-1:
                return count
            
            mini = float('inf')

            for nei in graph[node]:
                result = DFS(nei, count + 1)
                mini = min(mini, result)
            
            return mini
            
            

        for node in range(len(queries)):
            graph[queries[node][0]].append(queries[node][1])
            a = DFS(0, 0)
            result.append(a)
        
        return result


###################################### Solution Passed 972/972 Test Cases #############################
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        result = []
        graph = [[] for _ in range(n)]
        for i in range(n-1):
            graph[i].append(i+1)
        
        def BFS():
            distances = [-1] * n
            distances[0] = 0

            queue = deque([0])
            while queue:
                node = queue.popleft()

                for nei in graph[node]:
                    if distances[nei] == -1:

                        distances[nei] = distances[node] + 1
                        queue.append(nei)

                        if nei == n-1:
                            return distances[n-1]
                
            return distances[n-1]
             
            
            

        for u, v in queries:
            graph[u].append(v)
            a = BFS()
            result.append(a)
        
        return result
