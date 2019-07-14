# How could you represent 3 stacks using just 1 array


# With Stack class, instantiate 3 Stack objects
# and push them into positions 0, 1, and 2 .

# We can index each stack class in O(1)

from stack import Stack

arr = []
for i in range(3):
    arr.append(Stack())

arr[0].push(10)
arr[1].push(12)
arr[2].push(17)

print(f'popped from second stack value {arr[1].pop()}')