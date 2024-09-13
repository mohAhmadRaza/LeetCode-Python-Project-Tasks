# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev, curr = head, head.next
        index = []
        pos = 1

        while curr.next:
            if prev.val < curr.val > curr.next.val or prev.val > curr.val < curr.next.val:
                index.append(pos)
            pos += 1
            curr = curr.next
            prev = prev.next
        
        if len(index) < 2:
            return [-1, -1]
        
        mini,maxi = float('inf'), index[-1] - index[0]
        for i in range(1, len(index)):
            mini = min(mini, abs(index[i] - index[i-1]))
        
        return [mini, maxi]

        
