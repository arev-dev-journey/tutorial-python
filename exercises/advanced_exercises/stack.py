class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        '''Add item to the top of the stack'''
        self.stack.append(item)

    def pop(self):
        '''Remove and return to the top item. Raise IndexError if empty'''
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()

    def peek(self):
        '''Return the top item without removing it'''
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.stack[-1]
    def is_empty(self):
        '''Check if stack is empty'''
        return len(self.stack) == 0

    def size(self):
        '''Return the number of items in the stack'''
        return len(self.stack)
    def __str__(self):
        '''String representation of the stack (top at the end)'''
        return str(self.stack)

    def hello_world(self):
        pass

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack)
print(stack.pop())
print(stack.peek())
print(stack.size())
print(stack.pop())
print(stack.pop())
print(stack)
stack.push(40)
print(stack)
