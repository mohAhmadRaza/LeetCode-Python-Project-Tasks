# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        L = set()
        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            L.add(node.val)
            inorder(node.right)
        
        inorder(root)
        
        if len(L) < 2:
            return -1
        else:
            sort = sorted(L)
            return sort[1]
