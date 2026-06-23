class Stack:
    def __init__(self):
        self.items = []

    def push(self,data):
        self.items.append(data)

    def pop(self):
        if len(self.items) == 0:
            print("Stack is Empty.")
            return
        
        return self.items.pop()
    
    def peek(self):
        if not self.items:
            print("List is Empty")
            return
        
        return self.items[-1]
    
    def isEmpty(self):
        if not self.items:
            return True
        
        return False

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.items)

s.pop()
print(s.items)
print(s.peek())

print(s.isEmpty())