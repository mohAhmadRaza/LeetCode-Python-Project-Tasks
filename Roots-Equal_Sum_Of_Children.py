# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if root.left and root.right and root.val == ( root.left.val + root.right.val ):
            return True
        elif root.left and root.right and root.val != ( root.left.val + root.right.val ):
            return False
        
        return checkTree(root.left) and checkTree(root.right)
        
