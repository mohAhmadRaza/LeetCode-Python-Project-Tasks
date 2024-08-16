class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Calculating Destination
        dest = len(graph) - 1

        # Array to store all the paths
        result = []

        # traversing through DFS
        def DFS(currNode, vis, array):

            # If destination occurs, add the path to the result
            if currNode == dest:
                result.append(array.copy())
                return

            # Mark the current node as visited
            vis[currNode] = True
            
            # Start traversing through the neighbours of curr node
            for neighbour in graph[currNode]:

                # Check if the neighbour is visited or not
                if not vis[neighbour]:

                    # If not append it into path
                    array.append(neighbour)

                    # Call recursive DFS on the neighbours
                    DFS(neighbour, vis, array)

                    # After adding into path and appending path into result, pop it from path
                    array.pop()
            
            # Make the node unvisited
            vis[currNode] = False
        
        # Calling DFS from the source
        vis = [False] * (dest+1)
        array = [0]
        DFS(0, vis, array)
        
        return result
        
                
            

