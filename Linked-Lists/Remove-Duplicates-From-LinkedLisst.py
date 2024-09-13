# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        t = ListNode(0)
        answer = t

        while temp:
            if temp.next and temp.val == temp.next.val:
                val = temp.val
                while temp and temp.val == val:
                    temp  = temp.next
            else:
                answer.next = temp
                answer = answer.next
                temp = temp.next
        
        answer.next = None
        return t.next
