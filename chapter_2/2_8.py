# Given linked list, check if there is a loop
# (loop means list contains 2 references to same node)
# If there is a loop return the node at the start of the loop



# Big O
    # O(N) worst case to see if loop exists
    # O(N - 1) worst case to find beginning of loop

    # O(2) best case for checking if loop exists
    # O(1) best case for find start of loop

    # runtime: O(N)


from linked_list import LinkedList, Node



def find_loop(linked_list):
    if (linked_list.length == 0):
        return None
    head = linked_list.head
    loop_value = None
    lookup = {}
    while(head):
        key = str(head.value)
        if (key in lookup):
            loop_value = key
            break
        lookup[key] = True
        head = head.next
    # No loop found
    if (not loop_value): 
        return None
    # Find the beginning of the loop
    head = linked_list.head
    while(head):
        if (str(head.value) == loop_value):
            return head
        head = head.next
    return None






shared_node = Node(10)
lst2 = LinkedList()

lst2.insert(8)
lst2.insert(5)
lst2.insert_node(shared_node)
lst2.insert(4)
lst2.insert(7)
lst2.insert(2)
lst2.insert(0)
lst2.insert(3)
lst2.insert(8)

print(lst2)
loop_node = find_loop(lst2)
if (not loop_node):
    print('no loop found')
else:
    print(f'loop found with value {loop_node.value}')    
