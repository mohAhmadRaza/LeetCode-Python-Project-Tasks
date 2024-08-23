# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        s = set()
        def inOrder(node):
            if not node:
                return None
            
            inOrder(node.left)
            s.add(node.val)
            inOrder(node.right)

        inOrder(root)
        return len(s) == 1
