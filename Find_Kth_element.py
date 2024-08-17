class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        
        while True:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Pop the node from the stack
            current = stack.pop()
            k -= 1
            
            # If k is 0, we've found the k-th smallest element
            if k == 0:
                return current.val
            
            # Move to the right node
            current = current.right

Method 2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inOrderTraversal(node, array):
            if not node:
                return None
            
            inOrderTraversal(node.left, array)
            array.append(node.val)
            inOrderTraversal(node.right, array)
        

        array = []
        inOrderTraversal(root, array)
        return array[k-1]
            


