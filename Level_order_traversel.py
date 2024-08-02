# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        L = []
        Q = deque([root])

        while Q:
            Level = []
            for i in range(len(Q)):
                currentNode = Q.popleft()
                Level.append(currentNode.val)
                
                if currentNode.left:
                    Q.append(currentNode.left)
                
                if currentNode.right:
                    Q.append(currentNode.right)
            
            L.append(Level)
        
        return L
            


