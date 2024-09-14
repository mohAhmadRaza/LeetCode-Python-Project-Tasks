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
