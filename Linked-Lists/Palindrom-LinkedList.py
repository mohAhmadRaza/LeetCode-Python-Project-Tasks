# Your task is to check if given linkedlist
# is a pallindrome or not.
	
# Function Arguments: head (reference to head of the linked list)
Return Type: boolean , no need to print just return True or False.

# Node Class
  class Node:
      def __init__(self, data):   # data -> value stored in node
          self.data = data
          self.next = None

#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        stack = []
        temp = head
        
        while temp:
            stack.append(temp.data)
            temp = temp.next
        
        temp= head
        while temp:
            if temp.data != stack.pop():
                return False
            temp = temp.next
            
        return True
