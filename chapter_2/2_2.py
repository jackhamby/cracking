# Implement alg to find the kth to last element of a
# linkedlist 

# Assumption:
    # My LinkedList keeps track of its length

# Big O
    # where N is length of linked list
    # O(N) 
    # worst case is O(N) if its 0th to last element
    # best case is O(1) if its Nth to last element

from linked_list import LinkedList

lst = LinkedList()

lst.insert(5)
lst.insert(2)
lst.insert(2)
lst.insert(4)
lst.insert(5)
lst.insert(8)


def find(linked_list, k):
    if (not linked_list.head):
        return -1
    if (linked_list.length < k):
        return -1
    index = linked_list.length - k
    head = linked_list.head
    nxt = head.next
    i = 0
    while(i < index and nxt):
        head = nxt
        nxt = nxt.next
        i += 1
    return head.value

print(lst)
result = find(lst, 0)
print(result)