


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        if (not self.head):
            return "[]"
        if (not self.head.next):
            return f'[{self.head.value}]'
        output = f'{self.head.value},'
        head = self.head
        nxt = self.head.next
        while(nxt):
            if (nxt.next):
                output += f'{nxt.value},'
            else:
                output += f'{nxt.value}'
            head = nxt
            nxt = head.next
        return f'[{output}]'

    def insert(self, value):
        if (not self.head):
            self.head = Node(value)
            self.tail = self.head
            return self.head
        head = self.head
        while(head):
            if (not head.next):
                head.next = Node(value, head)
                self.tail = head.next
                return self.head
            head = head.next

        


class Node:

    def __init__(self, value, prev=None):
        self.next = None
        self.prev = prev
        self.value = value

    

lst = LinkedList()
lst.insert(2)
lst.insert(4)
lst.insert(5)
lst.insert(7)
print(lst)
print(f'head value {lst.head.value}')
print(f'tail value {lst.tail.value}')
