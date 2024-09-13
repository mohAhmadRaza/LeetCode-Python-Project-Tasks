# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        heap = []
        
        def DFS(currNode, count):
            if not currNode.left and not currNode.right:
                heapq.heappush(heap, count)
                return
            
            if currNode.left:
                DFS(currNode.left, count+1)
            
            if currNode.right:
                DFS(currNode.right, count + 1)
        
        DFS(root, 1)
        return heapq.heappop(heap)

// Method ## 2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = []
        
        def DFS(currNode, count):
            if not currNode.left and not currNode.right:
                result.append(count)
                return
            
            if currNode.left:
                DFS(currNode.left, count+1)
            
            if currNode.right:
                DFS(currNode.right, count + 1)
        
        DFS(root, 1)
        return min(result)
