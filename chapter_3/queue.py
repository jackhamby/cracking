

class Queue:

    def __init__(self):
        self.front = None
        self.back = None

    def __repr__(self):
        string = ""
        if (not self.front):
            return "[]"
        head = self.front
        while(head):
            if (not head.next):
                string += f'{head.value}'
            else:
                string += f'{head.value},'
            head = head.next
        return f'[{string}]'


    def add(self, value):
        item = QueueItem(value)
        if (not self.back):
            self.front = item
            self.back = self.front
            return self.back
        self.back.next = item
        item.prev = self.back
        self.back = item
        return self.back

    def remove(self):
        if (not self.front):
            return None
        data = self.front.value
        if (not self.front.next):
            self.front = None
            self.back = None
            return data
        self.front.next.prev = None
        self.front = self.front.next
        return data

        
    
        


 
class QueueItem:

    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value



queue = Queue()
queue.add(5)
queue.add(6)
queue.add(15)
print(queue)
queue_vals = []
queue_vals.append(queue.remove())
queue_vals.append(queue.remove())
queue_vals.append(queue.remove())
print('removed all values')
print(queue_vals)



queue.add(2)
queue.add(2)
queue.add(21)
queue.add(1)
queue.add(7)
queue.add(1002)

print(queue)