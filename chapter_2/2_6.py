# Given a string represented by a linked list, check if that string
# is a palindrome

# Big O
    # Runs at most O(n/2) only needing to iterate halfway 
    # through list (with 2 iterators, one in back one in front)

from doubly_linked_list import LinkedList
import math

def is_palidrome(linked_list):
    n = linked_list.length
    i, k = 0, n
    j = 1
    if (n == 0 or n == 1):
        return True

    head = linked_list.head
    tail = linked_list.tail
    
    while (j <= math.floor(n/2)):
        if (head.value != tail.value):
            return False
        head = head.next
        tail = tail.prev
        j += 1
    return True




lst = LinkedList()

lst.insert('t')
lst.insert('a')
lst.insert('c')
lst.insert('o')
lst.insert('c')
lst.insert('a')
lst.insert('t')


lst2 = LinkedList()

lst2.insert('t')
lst2.insert('a')
lst2.insert('c')
lst2.insert('o')
lst2.insert('c')
lst2.insert('a')
lst2.insert('b')


print(lst)
print(is_palidrome(lst))

print(lst2)
print(is_palidrome(lst2))

