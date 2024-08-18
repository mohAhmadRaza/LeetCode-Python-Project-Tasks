class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Creating an empty adjacency List to store graph vertices and destinations
        graph = [[] for _ in range(numCourses)]
        
        # Adding destinations of corresponding vertices
        for u, v in prerequisites:
            graph[u].append(v)
        
        # Checking if the graph contains a cycle making impossible to complete all courses 
        def isCycle(currNode, vis, rec):

            # Adding nodes into visisted and recurrision stack to find cycles
            vis[currNode] = True
            rec[currNode] = True
            
            # Applying same rule on all the neighbours of the current node
            for nei in graph[currNode]:
                if rec[nei]:
                    return True
                
                elif not vis[nei]:
                    if isCycle(nei, vis, rec):
                        return True
            
            rec[currNode] = False
            return False
        
        vis = [False] * numCourses
        rec = [False] * numCourses

        for node in range(numCourses):
            if not vis[node]:

                # If any cycle found means impossible to finish all courses, hence returning
                # List, means no courses
                if isCycle(node, vis, rec):
                    return []
        
        # If there's no cycle means can arrange the courses in child -> parent form
        def topologicalSort(currNode, visited, array):
            visited[currNode] = True
            
            # Aplying for loop on the neighbours
            for neighbour in graph[currNode]:

                # If I found any neighbour which is already visited
                # I will never visit that again
                if not visited[neighbour]:
                    topologicalSort(neighbour, visited, array)
            
            # Appedning the node which has no childes
            array.append(currNode)
        
        # Calling functions
        array = []
        visited_topo = [False] * numCourses
        for node in range(numCourses):
            if not visited_topo[node]:
                topologicalSort(node, visited_topo, array)
        
        return array
