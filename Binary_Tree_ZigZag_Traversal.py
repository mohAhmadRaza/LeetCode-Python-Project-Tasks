# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # For Level Order Traversing, We are going to use BST
        # Creating a Queue For FIFO
        queue = deque([root])
        
        # List to store result
        result = []
        reverse = False

        while queue:
            elements = []
            length = len(queue)

            for i in range(length):
                currNode = queue.popleft()
                elements.append(currNode.val)

                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)

            result.append(elements if not reverse else elements[::-1])
            reverse = not reverse

        return result


Method 2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # For Level Order Traversing, We are going to use BST
        # Creating a Queue For FIFO
        queue = deque([root])
        
        # List to store result
        result = []
        j = 0

        while queue:
            elements = []
            length = len(queue)

            for i in range(length):
                currNode = queue.popleft()
                elements.append(currNode.val)

                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            
           j += 1
           if j % 2 == 1:
              result.append(elements)
           else:
              result.append(elements[::-1]


        return result
