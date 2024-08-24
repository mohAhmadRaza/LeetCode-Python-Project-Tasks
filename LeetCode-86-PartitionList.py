# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp = head
        LesserElements, GreaterElements = ListNode(0), ListNode(0)
        temp2, temp3 = LesserElements, GreaterElements

        while temp:
            if temp.val < x:
                temp2.next = temp
                temp2 = temp2.next
            else:
                temp3.next = temp
                temp3 = temp3.next
            # Move to the next node in the original list
            temp = temp.next

        # End the list to avoid cycles
        temp3.next = None
        temp2.next = GreaterElements.next

        return LesserElements.next
