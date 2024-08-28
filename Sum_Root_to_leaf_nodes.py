# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Helper function to perform DFS
        def DFS(node, current_sum):
            if not node:
                return 0

            # Update the current path sum by adding the current node's value
            current_sum = current_sum * 10 + node.val

            # If it's a leaf node, return the current sum
            if not node.left and not node.right:
                return current_sum

            # Recursively calculate the sum for left and right subtrees
            left_sum = DFS(node.left, current_sum)
            right_sum = DFS(node.right, current_sum)

            # Return the total sum
            return left_sum + right_sum

        # Start the DFS from the root with an initial sum of 0
        return DFS(root, 0)

'''
Method 2
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
             return root.val
        
        def DFS(node, string):
            if not node:
                return string

            string += str(node.val)
            
            if not node.left and not node.right:
                return string
            
            LeftString = DFS(node.left, string)
            RightString = DFS(node.right, string)

            if not LeftString:
                LeftString = '0'
            if not RightString:
                RightString = '0'
            
            return int(LeftString) + int(RightString)
        
        return DFS(root, "")
