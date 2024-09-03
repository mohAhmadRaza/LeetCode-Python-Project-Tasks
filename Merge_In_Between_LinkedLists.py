# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp = list1
        newList = ListNode(0)
        curr = newList
        count = 0

        while count < a:
            count += 1
            curr.next = temp
            temp = temp.next
            curr = curr.next
        
        while list2:
            curr.next = list2
            curr = curr.next
            list2 = list2.next
        
        while count < b:
            count += 1
            temp = temp.next
        
        curr.next = temp.next
        return newList.next
        
        




            
