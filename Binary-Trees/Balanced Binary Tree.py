# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # LeftSum, RightSum = 0, 0
        if not root:
            return True

        def HeightBalanced(currNode):

            if not currNode:
                return 0
            
            LeftSum = HeightBalanced(currNode.left)
            if LeftSum == -1:
                return -1

            RightSum = HeightBalanced(currNode.right)
            if RightSum == -1:
                return -1

            if not abs( LeftSum - RightSum ) <= 1:
                return -1

            return max(LeftSum, RightSum) + 1
        
        return HeightBalanced(root) != -1
        





