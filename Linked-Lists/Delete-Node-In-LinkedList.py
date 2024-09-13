# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        # As we don't have aaccess of head, we have node which to delete not from memory, but from
        # Linked List, so I am just copying the value of next node amd storing it in curr one
        node.val = node.next.val

        # And then remving the next node as it's val already copied in previous node
        node.next = node.next.next
        
