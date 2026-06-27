from collections import deque

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,data):
        self.items.append(data)
    
    def pop(self):
        if len(self.items) == 0:
            print("stack is Empty")
        
        s_popped = self.items.pop()
        return s_popped
    
    def display(self):
        if len(self.items) == 0:
            print("stack is Empty")
        stack = []
        for items in self.items:
            stack.append(str(items))

        print(" -> ".join(stack)+"-> Head") 


class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self,data):
        self.items.append(data)
        
    def display(self):
        for items in self.items:
            print(items)

    def dequeue(self):
        if len(self.items) == 0:
            print("Queue is Empty")
            return
        popped = self.items.popleft()
        return popped
    
    def is_empty_check(self):
        if len(self.items) != 0:
            return False
        return True
    
    def reverse(self):
        temp_stack = Stack()
        
        while not self.is_empty_check():
            temp_stack.push(self.dequeue())
        
        while len(temp_stack.items) > 0:
            self.enqueue(temp_stack.pop()) 
        
       
        

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.display()
print("---")
q.reverse()
q.display()