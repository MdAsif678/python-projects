from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self,data):
        self.items.append(data)
        return data
    
    def dequeue(self):
        if not self.items:
            print("Queue is Empty")
            return

        return self.items.popleft()
    
    def isEmpty(self):
        if not self.items:
            return True
        
        return False
    
    def display(self):
        if not self.items:
            print("Queue is Empty")
            return
        
        print(self.items)
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.display()

q.dequeue()
q.dequeue()
q.display()

print(q.isEmpty())
