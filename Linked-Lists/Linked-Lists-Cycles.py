# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        iterator = head

        while iterator:
            if iterator in seen:
                return True
            seen.add(iterator)
            iterator = iterator.next
        
        return False
