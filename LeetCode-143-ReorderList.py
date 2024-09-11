# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # Initially pointing different variables to head
        slow, fast = head, head
        
        # Finding mid of the linkedlist
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # As, we have to take vlue after the mid, so moving slow one place
        # To get the value right after the mid value
        curr = slow.next

        # As we will adding next nalues of mid in start, so making mid's next to None
        slow.next = None
        
        # Now, it;s logic to reverse linkedlist
        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        # Now, starting from start and adding reversed list element with it
        temp = head
        while prev:
            newNode = ListNode(prev.val)
            newNode.next = temp.next
            temp.next = newNode

            prev = prev.next
            temp = temp.next.next
        

        



        
        
