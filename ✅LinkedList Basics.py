## initialize Single linkedList ---------------------------------------------------------------
class Node:
    def __init__( self , data ):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        head = self.head
    
    def traversal(self):
        head = self.head
        while head is not None:
            print(head.data)
            head = head.next
ll = LinkedList()
ll.head = Node(5)
first = Node(12)
second = Node(21)

ll.head.next = first
first.next = second

print(ll.traversal())
