# given unsorted linked list, remove all duplicates

# Big O
    # Let N be the size of the linked_list
    # O(N) because we traverse the linked list just once
        # Each node we traverse we also attempt insert into
        # buffer hash table, which worst case would be O(N)
        # but average case is O(1) 

from linked_list import LinkedList

lst = LinkedList()

lst.insert(5)
lst.insert(2)
lst.insert(2)
lst.insert(4)
lst.insert(5)
lst.insert(8)

def insert_buffer(buffer, value):
    val = str(value)
    if (val in buffer):
        return False
    buffer[val] = True
    return True

def remove_duplicates(linked_list):
    buffer = {}
    head = linked_list.head
    if (not head):
        return linked_list
    insert_buffer(buffer, head.value)
    nxt = head.next
    while(nxt):
        if (not insert_buffer(buffer, nxt.value)):
            head.next = nxt.next
            nxt = head.next
        else:
            head = nxt
            nxt = nxt.next



print(f'list before {lst}')
remove_duplicates(lst)
print(f'list after {lst}')