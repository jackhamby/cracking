
class Stack:


    def __init__(self):
        self.top = None

    def __repr__(self):
        top = self.top
        string = "STACK \n"
        while(top):
            string += f'{top.data}\n'
            top = top.next
        return string

    def push(self, data):
        item = StackItem(data)
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
        return data

    def peek(self):
        if (not self.top):
            return -1
        return self.top.data


class StackItem:

    def __init__(self, data):
        self.data = data
        self.next = None
        



# stack = Stack()
# stack.push(2)
# stack.push(4)
# print(stack)

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