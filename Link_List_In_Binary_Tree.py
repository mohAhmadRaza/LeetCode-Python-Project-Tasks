# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        L = []
        temp = head
        while temp:
            L.append(temp.val)
            temp = temp.next
        
        def dfs(nod, idx):
            if not nod:
                return False
            
            if nod.val == L[idx]:
                idx += 1
                if idx == len(L):
                    return True
            if dfs(nod.left, idx) or dfs(nod.right, idx):
                return True
            return False

        def check(node):
            if not node:
                return False
            
            if dfs(node, 0):
                return True
            
            return check(node.left) or check(node.right)
        
        return check(root)
                   

            
            

        
