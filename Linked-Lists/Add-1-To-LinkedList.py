#User function Template for python3

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def addOne(self,head):
        temp = head
        string = ""
        
        while temp:
            string += str(temp.data)
            temp = temp.next
        
        number = int(string) + 1
        
        newnode = Node(0)
        curr = newnode
        
        for i in str(number):
            node = Node(int(i))
            curr.next = node
            curr = curr.next
        
        return newnode.next

                                                   #########   Method : 2  #########
#User function Template for python3

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def addOne(self,head):
        temp = head
        
        def reverse(head):
            prev = None
            temp = head
            
            while temp:
                newnode = temp.next
                temp.next = prev
                prev = temp
                temp = newnode
            
            return prev
        
        head = reverse(head)
        temp = head
        carry = 1
        
        while temp and carry:
            if temp.data >= 9:
                temp.data = 0
                if not temp.next:
                    temp.next = Node(1)
                    carry = 0
                else:
                    temp.next.data += 1
                    carry = 1 if temp.next.data > 9 else 0
            elif temp.data < 9:
                temp.data += 1
                carry = 0
            
            temp = temp.next
