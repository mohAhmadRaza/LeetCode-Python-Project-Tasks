# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        count = 0
        temp = head

        result = []
        i = 0
        while temp:
            if temp.val in nums:
                i += 1
                
            else:
                if i != 0:
                   result.append(i)
                i = 0
            temp = temp.next
        
        if i > 0:
            result.append(i)
        return len(result)
