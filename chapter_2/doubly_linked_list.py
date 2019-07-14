


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

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
        self.length += 1
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

    def remove(self, value):
        if (not self.head):
            return self.head
        if (self.head.value == value):
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return self.head
        head = self.head
        nxt = head.next
        while(nxt):
            if (nxt.value == value):
                head.next = nxt.next
                self.length -= 1
                if (not head.next):
                    self.tail = head
                    return
                head.next.prev = head
                return
            head = nxt
            nxt = head.next



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
lst.remove(7)
lst.insert(4)


print(lst)
print(f'head value {lst.head.value}')
print(f'tail value {lst.tail.value}')
