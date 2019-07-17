# How would you implement a stack that has a min function?
# so the stack has push(), pop() and min() all must be O(1)

# Big O
    # push() will remain O(1), it just do an additional
    # compare with Stack.min

    # pop() however may be O(n) if the smallest value 
    # was popped from the stack

    # min() is O(1) because it is just access a class
    # variable

import sys

class Stack:


    def __init__(self):
        self.top = None
        self.min = sys.maxsize

    def __repr__(self):
        top = self.top
        string = "STACK \n"
        while(top):
            string += f'{top.data}\n'
            top = top.next
        return string

    def push(self, data):
        item = StackItem(data)
        if (data < self.min):
            self.min = data
        if (not self.top):
            self.top = StackItem(data)
            return self.top
        item.next = self.top
        self.top = item
        return self.top
        
    def pop(self):
        if (not self.top):
            return -1
        data = self.top.data
        self.top = self.top.next
        if (data == self.min):
            self.min = self.get_min()
        return data

    def peek(self):
        if (not self.top):
            return -1
        return self.top.data

    def min(self):
        return self.min

    def get_min(self):
        minimum = sys.maxsize
        head = self.top
        while(head):
            if (head.data < minimum):
                minimum = head.data
            head = head.next
        return minimum



class StackItem:

    def __init__(self, data):
        self.data = data
        self.next = None
        



stack = Stack()
stack.push(2)
stack.push(4)
stack.push(6)
stack.push(1)
print(stack)
print(stack.min)
stack.pop()
print(stack.min)

# data = stack.pop()
# print(f'popped {data}')
# print(stack)

# stack.push(12)
# stack.push(11)
# stack.push(100)

# data = stack.peek()
# print(f'peeked top is {data}')
# print(stack)
# print(stack.top.data)
