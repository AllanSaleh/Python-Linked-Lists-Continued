# Python builtin stack is actually just a python list

# append() adds to the end of the list (aka top of the stack) - O(1)
# pop() removed the last thing added from the list - O(1)
# list[-1] is equivalent to peek (Look at the last item) - O(1)


# Why can't lists behave like a queue

# append() adds to the end of the list (aka end of the queue) - O(1)
# pop(0) while this removes the first item in the queue, it happens slowly - O(n) BIG PROBLEM
# list[0] is equivalent to peek (Looking at the first item in the queue) - O(1)

# Can treat a deque like queue
from collections import deque

queue = deque()

# Enqueue operation (add to the end of the queue)
queue.append("first")
queue.append("second")
queue.append("third")

print(f"Queue: {queue}")

# Dequeue operations (remove from front)
front_item = queue.popleft() #Happens in O(1) time IMPORTANT
print(f"Dequeued: {front_item}")
print(f"Queue after dequeueing: {queue}")