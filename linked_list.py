# A LInked list is made upn of Nodes connected together in a chain

# ------------------ NODE CLASS ----------------------
class Node:
  def __init__(self, data):
    # data is the information we want to store in the node
    self.data = data
    # next is a pointer (or reference) to the next node in the list
    # Initially its None because when we creat a node it doesnt point to anything
    self.next = None

# ----------------- Linked List Class ---------------------
# grocery = []
class LinkedList:
  def __init__(self):
    # head is the first node in the list
    # If the list is empty, head will be none
    self.head = None

    # tail is the last node in the list
    # If the list is empty, tail will be none
    # tail is used to make adding new nodes faster
    self.tail = None
  
  # Check if the linked list is empty
  def is_empty(self):
    return self.head is None
  
  # ----------------- APPEND METHOD -------------------
  def append(self, data):
    # step 1
    new_node = Node(data)

    # step 2: If the list is empty, the new node becomes both head and tail
    if self.is_empty():
      self.head = new_node
      self.tail = new_node
      return
    else:
      # Step 3: If the list already has nodes
      # Link the current tail to the new node
      self.tail.next = new_node

      # Step 4: Move the tail pointer to point to the new node (the new end of the list)
      self.tail = new_node

  # -------------- Traverse Method ------------------
  def traverse(self):
    print("============== List Contents ================")

    # CASE 1: If the list is empty, let the user know
    if self.is_empty():
      return "Sorry the list is empty"
    
    # CASE 2: Start from the head and keep following the 'next' until theres no more nodes
    # Step1: Create a 'current' marker pointing to the same node as the head
    current = self.head

    # Step 2: display data of that node and move to the next node
    while current != None:
      print(current.data)    #Print the current node's data
      current = current.next #Move to the next node in the chain
  
  # --------------- INSERT AT POSITION ---------------
  # Insert a new node at a specific position (1-based position)
  def insert_at_position(self, position, data):
    # Create the node with the data
    new_node = Node(data)

    # Case 1: Insert at the very beginning of the list (before the head)
    if position == 1:
      # self.append(data)
      new_node.next = self.head
      self.head = new_node

      # If the list was empty, update the tail too
      if self.tail is None:
        self.tail = new_node
      return

    # Case 2: Insert somewhere else in the list
    current = self.head
    counter = 1

    # Move to the current just before the desired position
    while counter < position - 1:
      current = current.next
      counter += 1

    # Insert the new node into the chain
    new_node.next = current.next # Step 1: New node points to the next node
    current.next = new_node #Step 2: Previous node points to new node
  
  # Deletes a node from a specific position
  def delete_at_position(self, position):
    # Case 1: If list is empty
    if self.is_empty():
      print("List is empty. Nothing to delete")
      return

    # Case 2: Deleting the head (first node)
    if position == 1:
      self.head = self.head.next #Move head to next node

      # If the list becomes empty, reset the tail as well
      if self.head is None:
        self.tail = None
      return
    
    # Case 3: Deleting at any other position
    current = self.head
    counter = 1
    # Move to the node just before the one we want to delete
    while counter < position - 1:
      current = current.next
      counter += 1

    # If deleting the last node, update the tail
    if current.next == self.tail:
      self.tail = current
    
    # Skip over the deleted node
    removing = current.next
    current.next = current.next.next
    return removing
  
  def get_at_position(self, position):
    counter = 1
    current = self.head # starting from the front of the list
    while counter < position:
      if current is None or current.next is None:
        print("Position out of bounds")
        return
      current = current.next
      counter += 1
    
    # If position is out of range

    return current.data

# Create a new linked list
my_list = LinkedList()

# Append items
my_list.append("Apple")
my_list.append("Banana")
my_list.append("Cherry")

my_list.insert_at_position(1, "Pears")
my_list.insert_at_position(3, "Mangos")

my_list.delete_at_position(1)

my_list.delete_at_position(4)
my_list.delete_at_position(2)

# Print list contents
my_list.traverse()
