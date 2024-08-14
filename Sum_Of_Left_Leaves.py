# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        q = deque()
        q.append(root)

        while q:
            length = len(q)

            for _ in range(length):
                curr = q.popleft()

                if curr.left:
                    if not curr.left.left and not curr.left.right:
                        total += (curr.left.val)
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        
        return total
