## initialize Single linkedList ---------------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        head = self.head
        while head is not None:
            print(head.data, "-->", end=" ")
            head = head.next
        print("Null")  # End of the list
    
    def insert_in_beg(self, data):
        node_beg = Node(data)
        node_beg.next = self.head
        self.head = node_beg
        
    def insert_in_end(self, data):
        node_end = Node(data)
        # If the list is empty
        if self.head is None:
            self.head = node_end
            return
        
        # Traverse to the last node
        head = self.head
        while head.next is not None:
            head = head.next
        
        # Link the last node to the new node
        head.next = node_end

# Creating the LinkedList
ll = LinkedList()
ll.head = Node(5)
first = Node(10)
second = Node(15)

# Linking the nodes
ll.head.next = first
first.next = second

# Inserting new nodes
ll.insert_in_beg(1)  # Insert 1 at the beginning
ll.insert_in_end(20)  # Insert 20 at the end

# Traverse and print the list
ll.traversal()
