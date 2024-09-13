# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        temp = head
        odds = ListNode()
        o = odds
        evens = ListNode()
        e = evens
        i = 0
        while temp:
            if (i+1) % 2 == 1:
                o.next = temp
                o = o.next
            else:
                e.next = temp
                e = e.next
            temp = temp.next
            i += 1
        
        e.next = None
        o.next = evens.next
        return odds.next
