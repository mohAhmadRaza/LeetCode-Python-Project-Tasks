# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def Countgood(node, max_value):
            if not node:
                return 0
            
            good = 0
            if node.val >= max_value:
                good = 1
                max_value = node.val
            
            good += Countgood(node.left, max_value)
            good += Countgood(node.right, max_value)

            return good

        return Countgood(root, root.val)
