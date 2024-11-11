# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        complement  = set()

        def DFS(currNode):

            if not currNode:
                return False
            
            if currNode.val in complement:
                return True

            complement.add(k - currNode.val)

            return (DFS(currNode.left) or DFS(currNode.right))
        
        return DFS(root)

####################################### Solution : 2 ####################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        complement = defaultdict(int)

        def DFS(currNode):

            if not currNode:
                return False
            
            if currNode.val not in complement.keys():
                complement[k-currNode.val)] = currNode.val

            else:
                return True

            return (DFS(currNode.left) or DFS(currNode.right))
        
        return DFS(root)
