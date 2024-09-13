# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        curr = head
        answer = curr

        maximum = 0
        while curr and prev:
            maximum= max(maximum, curr.val + prev.val)
            curr = curr.next
            prev = prev.next
        
        return maximum
