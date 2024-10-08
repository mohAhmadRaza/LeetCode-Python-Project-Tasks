# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        fast = fast.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if slow:
            slow.next = slow.next.next
        
        return head

        
            
Method 2:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        pos = 0

        if not head or not head.next:
            return None

        while temp:
            pos += 1
            temp = temp.next
        
        ele_before_mid =( pos // 2 )
        temp = head

        # Step 2: Traverse the list to the node before the middle
        temp = head
        for _ in range(ele_before_mid - 1):
            temp = temp.next
        
        if temp:
           temp.next = temp.next.next
        
        return head
