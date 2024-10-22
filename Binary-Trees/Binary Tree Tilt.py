# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        tiltSum = 0
        def CountDiff(currNode):
            nonlocal tiltSum
            
            if not currNode:
                return 0
            
            SumLeft = CountDiff(currNode.left)
            SumRight = CountDiff(currNode.right)

            tiltSum += abs(SumLeft - SumRight)
            
            return SumLeft + SumRight + currNode.val
        
        CountDiff(root)
        return tiltSum





