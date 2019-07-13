

# An algorithm to remove a middle node from
# a singly linked list (middle = not the first or last node)
# given just a reference to said node

# Big O
    # let N be length of linked list
    # O(N - 1) is worst case where node before last is selected
    # O(2) is best case where 2nd node is deleted
    # delete is O(1) and it occurs once


from linked_list import LinkedList


def delete(linked_list, node):
    if (not linked_list.head):
        return
    if (linked_list == node):
        linked_list.head = linked_list.head.next
        return        
    head = linked_list.head
    nxt = head.next
    while(nxt):
        if (nxt == node and nxt.next):
            head.next = nxt.next
            return
        head = nxt
        nxt = head.next
    return 

def get_node(linked_list, index):
    if (index >= linked_list.length):
        return False
    head = linked_list.head
    nxt = head.next
    for i in range(index):
        head = nxt
        nxt = head.next
    return head


        

lst = LinkedList()
lst.insert(1) # 0
lst.insert(0) # 1
lst.insert(1) # 2 
lst.insert(3) # 3
lst.insert(5) # 4
lst.insert(1) # 5

print(lst)

# delete node at index 2
node = get_node(lst, 5)
if (node):
    delete(lst, node)

print(lst)



