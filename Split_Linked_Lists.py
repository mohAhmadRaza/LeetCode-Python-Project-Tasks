# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        elePerIndex = count // k
        remains = count % k

        result = []

        temp = head
        for i in range(k):
            part_head = temp
            size = elePerIndex + (1 if remains > 0 else 0)
            remains -= 1 if remains > 0 else 0 

            for j in range(size-1):
                if temp:
                   temp = temp.next
            
            if temp:
                nextPart = temp.next
                temp.next = None
                temp = nextPart
            
            result.append(part_head)
        
        while len(result) < k:
            result.append(None)
        
        return result

            

            


        

