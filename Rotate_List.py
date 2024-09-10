# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Checking if the LinkedList is empty or contains one element
        if not head or not head.next:
            return head

        # Initialization to find size of List
        temp, size = head, 0
        
        # Calculating Size of list
        while temp:
            size += 1
            temp = temp.next
        
        # reducing the number of rotations
        k = k % size
        if k == 0:
            return head
        
        # Move the temp until the node from which to onward we have to rotate
        temp = head
        count = 1
        while temp and count < size - k:
            count += 1
            temp = temp.next
        
        # Storing temp's next node in new head
        new_head = temp.next

        # Set it to None, as we rotated remaing list
        temp.next = None
        
        # adding head to rotated list
        temp = new_head
        while temp.next:
            temp = temp.next
        temp.next = head
        
        return new_head
