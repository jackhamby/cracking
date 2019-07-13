

# Sum lists
# Input is 2 integers, represented by linked lists
# The ints are in reversed order, so
    # (7 -> 1 -> 6) + (5 -> 9 -> 2)
    # 617 + 295

# Big O
    # let N be the size of num1, let K be the size of num2
    # O(N) + O(K)
    # So if we assume N >= K then we have O(N)

from linked_list import LinkedList
from math import pow


def add(num1, num2):
    value1 = add_list(num1)
    value2 = add_list(num2)
    return int(value1 + value2)

def add_list(linked_list):
    if (linked_list.length == 0):
        return 0
    power = 0
    head = linked_list.head
    nxt = head.next
    total_value = head.value * pow(10, power)
    power += 1
    while(nxt):
        total_value += nxt.value * pow(10, power)
        power += 1
        head = nxt
        nxt = head.next
    return total_value


num1 = LinkedList()
num2 = LinkedList()

num1.insert(7)
num1.insert(1)
num1.insert(6)

num2.insert(5)
num2.insert(9)
num2.insert(2)


result = add(num1, num2)
print(result)
