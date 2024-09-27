############################ Method 1 ##################

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first=edges[0][0]
        second=edges[0][1]
        if edges[1][0]==first or edges[1][1]==first:
            return first
        return second

########################### Method 2 ##################

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]


########################### Method 3 ##################
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        freq = defaultdict(int)
        maxi, ans  = 0, 0
        
        for a, b in edges:
            freq[a] += 1
            freq[b] += 1

        for a, b in freq.items():
            if b > maxi:
                ans, maxi = a, b
        
        return ans

