

class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0


    def __repr__(self):
        head = self.head
        string = "["
        while(head):
            if (not head.next):
                string += f'{head.value}'
            else:
                string += f'{head.value},'
            head = head.next
        string += "]"
        return string

    def insert(self, value):
        self.length += 1
        if (not self.head):
            self.head = Node(value)
            return self.head
        head = self.head
        while(head):
            if (not head.next):
                head.next = Node(value)
                return self.head
            head = head.next


    def insert_node(self, node):
        if (not self.head):
            self.head = node
            return self.head
        head = self.head
        while(head):
            if (not head.next):
                head.next = node
                return self.head
            head = head.next

        
    def remove(self, value):
        if (not self.head):
            return None

        if (self.head.value == value):
            self.head = self.head.next
            self.length -= 1
            return self.head

        head = self.head 
        nxt = self.head.next            
        while(nxt):
            if (nxt.value == value):
                head.next = nxt.next
                self.length -= 1
                return self.head
            head = nxt
            nxt = nxt.next



class Node:


    def __init__(self, value):
        self.next = None
        self.value = value






# lst = LinkedList()
# lst.insert(5)
# lst.insert(2)
# lst.insert(10)
# lst.remove(10)
# lst.remove(5)
# lst.remove(2)

# print(lst)






