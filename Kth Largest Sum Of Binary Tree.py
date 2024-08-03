# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        from collections import deque
        Queue = deque([root])
        Level = []

        while Queue:
            Length = len(Queue)
            sum = 0
            for i in range(Length):
                currentNode = Queue.popleft()
                sum += currentNode.val

                if currentNode.left:
                    Queue.append(currentNode.left)
                if currentNode.right:
                    Queue.append(currentNode.right)
            Level.append(sum)
        
        if len(Level) < k:
            return -1
        else:
            Level.sort(reverse=True)
            return Level[k-1]
            

                
