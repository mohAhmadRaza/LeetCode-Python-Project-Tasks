# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def check(node):
            if node.left is None and node.right is None:  # Leaf node
                return node.val == 1  # True if value is 1, otherwise False    

            left = check(node.left)
            right = check(node.right)

            if node.left and node.right:
                if node.val == 2:
                    return left or right
                else:
                    return left and right
        
        return check(root)
