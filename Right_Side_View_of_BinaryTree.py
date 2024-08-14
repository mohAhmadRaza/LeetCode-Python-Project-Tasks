# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
           return []

        array = []
        q = deque()
        q.append(root)

        while q:
            length = len(q)
            array.append(q[-1].val)
            for i in range(length):
                currNode = q.popleft()

                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
        
        return array
