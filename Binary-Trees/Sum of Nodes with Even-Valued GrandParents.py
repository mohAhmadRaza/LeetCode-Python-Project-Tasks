# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        sums = 0

        def DFS(currNode):
            nonlocal sums

            if not currNode:
                return 0
            
            if currNode.val % 2 == 0:
                if currNode.left:
                    if currNode.left.left:
                        sums += currNode.left.left.val
                    
                    if currNode.left.right:
                        sums += currNode.left.right.val
                
                if currNode.right:
                    if currNode.right.left:
                        sums += currNode.right.left.val
                    
                    if currNode.right.right:
                        sums += currNode.right.right.val
            
            DFS(currNode.left)
            DFS(currNode.right)
        
        DFS(root)

        return sums

                
