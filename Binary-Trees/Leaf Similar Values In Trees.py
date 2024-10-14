# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        FirstTree = []

        def FindTreeLeaves(node):
            if not node:
                return 0

            elif node and not node.right and not node.left:
                FirstTree.append(node.val)
            
            FindTreeLeaves(node.left)
            FindTreeLeaves(node.right)
            
        FindTreeLeaves(root1)
        First = FirstTree.copy()
        FirstTree = []
        FindTreeLeaves(root2)

        return First == FirstTree
