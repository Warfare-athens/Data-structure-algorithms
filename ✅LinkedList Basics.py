## Initialize Single LinkedList ---------------------------------------------------------------

class Node:
    def __init__( self , data ):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        head = self.head
        
    ## Travek in  linkedList ---------------------------------------------------------------
    
    def traversal(self):
        head = self.head
        while head is not None:
            print(head.data, "-->", end=" ")
            head = head.next
        print("Null")  # End of the list
        
    ## Insterion in  LinkedList ---------------------------------------------------------------
    def insert_in_beg(self , data):
        node_beg = Node(data)
        node_beg.next = self.head
        self.head = node_beg
        
    def insert_in_end(self , data):
        node_end = Node(data)
        
        if self.head is None:
            self.head = node_end
            return
        
        head = self.head
        while head.next is not None:
            head = head.next
        head.next = node_end
        
    def node_specific(self , data , position):
        node_at = Node(data)
        head = self.head
        curr = 0
        
        if head is None:
            node_at.next = head.next
            head = node_at
            return
        
        while curr < position-1:
            head = head.next
            curr += 1
        node_at.next = head.next
        head.next = node_at
        
    ## Deletion in  LinkedList ---------------------------------------------------------------
    def delete_beg(self):
        self.head = self.head.next
        
    def delete_end(self):
        head = self.head

        while head.next.next is not None:
            head = head.next
        head.next = None
        
    def delete_pos(self , position):
        head = self.head
        curr = 0
         
        while curr < position-1:
            head = head.next
            curr += 1
        head.next = head.next.next
        

        
ll = LinkedList()
ll.head = Node(5)
first = Node(10)
second = Node(15)

ll.head.next = first
first.next = second

print(ll.traversal())

ll.insert_in_beg(1)
print(ll.traversal())

ll.insert_in_end(20)
print(ll.traversal())

ll.node_specific(7 ,2)
print(ll.traversal())

ll.delete_beg()
print(ll.traversal())

ll.delete_end()
print(ll.traversal())

ll.delete_pos(2)
print(ll.traversal())
