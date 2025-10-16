class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.head = None #Top of the stack (most recently added)
    self.tail = None #Bottom of the stack (First thing added)
    self.size = 0

  def is_empty(self):
    return self.head is None
  
  def push(self, item):
    '''Adding an item to the top of the stack (head)'''

    new_node = Node(item)

    if self.is_empty():
      self.head = new_node
      self.tail = new_node
    else:
      # Add to the head (top of the stack)
      new_node.next = self.head
      self.head = new_node
    
    self.size += 1
    print(f"Pushed {item} onto the stack")
  
  def pop(self):
    '''Remove that last thing that was added to stack, and return it (head)'''
    if self.is_empty():
      print("Stack is empty!")
      return
    
    item = self.head.data
    self.head = self.head.next

    # if stack becomes empty, reset tail
    if self.head is None:
      self.tail = None
    
    self.size -= 1
    return item
  
  def peek(self):
    '''View top item in the stack without removing it'''
    if self.is_empty():
      print("Stack is empty")
      return
    return self.head.data

my_stack = Stack() #empty stack
my_stack.push("first")
my_stack.push("second")
my_stack.push("third")

print(my_stack.pop() + " was removed")

print(my_stack.peek())
