# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        res_cur = res = ListNode()
        cur = head
        num_set = set(nums)
        
        while cur:
            if cur.val not in num_set:
                res.next = ListNode(cur.val)
                res = res.next
            cur = cur.next
        
        return res_cur.next
