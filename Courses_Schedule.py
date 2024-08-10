class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Creating empty Lists in graph like structure i.e. in Adjacency Lists
        graph = [[] for _ in range(numCourses)]

        # Now storing the edges in previoulsy ceated graph
        for u, v in prerequisites:
            graph[u].append(v)
        
        # This array will check whether is already visited or not
        vis = [False] * numCourses

        # This will check whether the element is already in recursive stack
        rec = [False] * numCourses
        
        # Calling function for each node to check cycles
        def isCycle(curr, vis, rec):

            # Updating the values as true, so that we not use same again
            vis[curr] = True
            rec[curr] = True
            
            # Applying same rules on the neighbours of current node
            for neighbour in graph[curr]:

                # If neigbhour element is already in recursive stack, means cycle appeared now
                if rec[neighbour]:
                    return False
                
                # if not appeared then we will apply same rule on neigbhours
                elif not vis[neighbour]:
                    if not isCycle(neighbour, vis, rec):
                        return False
            
            # re truing the value
            rec[curr] = False
            return True
        
        for i in range(numCourses):
            if not vis[i]:
                if not isCycle(i, vis, rec):
                    return False
        return True
