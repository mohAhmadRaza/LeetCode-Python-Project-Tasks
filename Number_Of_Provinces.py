class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Count for number of provinces
        count = 0

        # Total Number of cities 
        numberOfCities = len(isConnected[0])

        # Array to keep the check which city has visited already
        vis = [False] * numberOfCities
         
        # Traversal for checking connection
        def DFS(currCity):
            vis[currCity] = True
            
            # Applying for loop on neighbours of current cities
            for nei in range(numberOfCities):
                if isConnected[currCity][nei] == 1 and not vis[nei]:
                    DFS(nei)

        # Checking connection from each city
        for city in range(numberOfCities):
            if not vis[city]:

                # If city is not connected then increment
                count += 1

                # And call DFS there on that city
                DFS(city)
        
        return count
