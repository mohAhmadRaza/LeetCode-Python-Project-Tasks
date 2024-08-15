# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
           return []

        array = []
        q = deque()
        q.append(root)

        while q:
            length = len(q)
            level_nodes = []

            for i in range(length):
                currNode = q.popleft()
                level_nodes.append(currNode.val)


                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
            
            array.append(level_nodes)
        
        return array[::-1]
        
