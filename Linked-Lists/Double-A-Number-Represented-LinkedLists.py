# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Check if the list is empty
        if not head:
            return None
            
        temp = head
        L =[]
        sys.set_int_max_str_digits(50000)
        while temp:
            L.append(str(temp.val))
            temp = temp.next
        
        s = ''.join(L)
        s = str(int(s)*2)

        answer = temp = ListNode()

        for i in s:
            temp.next = ListNode(int(i))
            temp = temp.next
        
        return answer.next
