# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        result = []

        def DFS(node, string):
            if not node:
                return 
            
            if string:
                string += "->" + str(node.val)
            else:
                string = str(node.val)

            if not node.left and not node.right:
                result.append(string)
                return
            
            DFS(node.left, string)
            DFS(node.right, string)
        
        DFS(root, "")

        return result
        

