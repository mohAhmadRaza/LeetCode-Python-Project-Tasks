# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([root])
        height = 0

        while q:
            XFound, YFound = False, False
            XParent, YParent = 0, 0
            length = len(q)

            for i in range(length):
                node = q.popleft()

                if node.left:
                    if node.left.val == x:
                        XFound = True
                        XParent = node.val
                    
                    elif node.left.val == y:
                        YFound = True
                        YParent = node.val
                    
                    q.append(node.left)
                
                if node.right:
                    if node.right.val == x:
                        XFound = True
                        XParent = node.val
                    
                    elif node.right.val == y:
                        YFound = True
                        YParent = node.val

                    q.append(node.right)
                
                if YFound and XFound and XParent == YParent:
                    XFound, YFound = False, False
            
            if XFound and YFound:
                return True
        
        return False
            
