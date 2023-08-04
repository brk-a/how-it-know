'''
implement a stack in py

stack: a list/queue that uses the LIFO principle

specs of a stack:
    1. add item to top of stack
    2. remove item from top of stack
    3. read the item at the top of the stack
'''

class Stack:
    """ class Stack: LIFO queue/list """
    def __init__(self):
        self.stack = []

    def push(self, item):
        """ add to stack """
        self.stack.append(item)

    def pop(self):
        """remove from stack"""
        return self.stack.pop()

    def read(self):
        """ read the item at the top of the stack """
        return self.stack[-1]

li = [i for i in range(50) if i % 2 == 0]
stack1 = Stack()
print(stack1.stack)
for i in li:
    stack1.push(i)
print(stack1.stack)
print(stack1.pop())
print(stack1.read())