class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node

    def display(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        print("Head -> " + " -> ".join(result) + " -> None")
    
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def search(self,data):
        current = self.head
        while current:
            if current.data == data:
                return True
            else:
                current = current.next
        
        return False
    
    def delete(self,data):
        if self.head is None:
            print("list is empty")
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        
        print("VAlue not FOund")
        

        


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.display()
ll.prepend(5)
ll.display()
print(ll.search(40))
print(ll.search(99))
ll.delete(10)
ll.display()

ll.delete(20)    
ll.display()

ll.delete(99)    
ll.display()

ll.delete(5)     
ll.display()