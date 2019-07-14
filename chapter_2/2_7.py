# Given 2 singly linked lists, return True if they
# intersect, False if they don't.
# Intersection is defined as sharing a node (by reference)


# Big O
    # given lst1, lst2 let N = lst1.length and K = lst2.length where lst1.length >= lst2.length
    # O(N) * O(K)



from linked_list import LinkedList, Node

def intersect(lst1, lst2):
    if (lst1.length == 0 or lst2.length == 0):
        return False
    main, secondary = (lst1, lst2) if lst1.length >= lst2.length else (lst2, lst1)
    head = main.head
    while(head):
        head2 = secondary.head
        while(head2):
            if (head2 == head):
                return True
            head2 = head2.next
        head = head.next
    return False


shared_node = Node(10)
lst1 = LinkedList()
lst2 = LinkedList()
lst3 = LinkedList()


lst1.insert(1)
lst1.insert(30)
lst1.insert_node(shared_node)

lst2.insert(4)
lst2.insert(4)
lst2.insert(4)
lst2.insert(4)
lst2.insert(4)
lst2.insert(4)
lst2.insert_node(shared_node)

lst3.insert(20)
lst3.insert(20)
lst3.insert(20)
lst3.insert(20)
lst3.insert(20)
lst3.insert(20)
lst3.insert(20)
lst3.insert(20)
lst3.insert(20)
lst3.insert(20)



# True
print(intersect(lst1, lst2))

# False
print(intersect(lst1, lst3))


# False  
print(intersect(lst3, lst1))

# False
print(intersect(lst3, lst2))    

# True
print(intersect(lst2, lst1))
