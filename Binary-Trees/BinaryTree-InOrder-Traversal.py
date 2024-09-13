# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    L = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None

        self.inorderTraversal(root.left)
        L.append(root.val)
        self.inorderTraversal(root.right)
    
        return L
