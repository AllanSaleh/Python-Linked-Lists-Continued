# In-Class Assignments - Stacks and Queues

## Assignment 1: Queue Implementation

### Overview
Now that you've mastered stack implementation, let's build a queue! Remember how we structured our stack with head and tail pointers? We'll use a similar approach, but with different behaviors for FIFO (First In, First Out).

This assignment builds directly on your stack knowledge - same linked list concepts, different access patterns!

### Queue vs Stack Comparison

Before implementing, let's think about the differences:

| Operation | Stack (LIFO) | Queue (FIFO) |
|-----------|--------------|--------------|
| **Add item** | Push to tail (top) | Enqueue to tail (rear) |
| **Remove item** | Pop from tail (top) | Dequeue from head (front) |
| **View next** | Peek at tail | Front at head |

### Your Task

Complete the missing methods in the Queue class:

```python
# Reuse the Node class from our stack implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None   # Front of queue (next item to be removed)
        self.tail = None   # Rear of queue (last item added)  
        self.size_count = 0
    
    def is_empty(self):
        """Check if queue has no elements"""
        return self.head is None
    
    def enqueue(self, item):
        """
        Add item to rear of queue (tail)
        
        Args:
            item: Data to add to the queue
        
        Hint: This is very similar to stack push, but we add to tail!
        """
        # YOUR IMPLEMENTATION HERE
        pass
    
    def dequeue(self):
        """
        Remove and return front item (head) - O(1) operation!
        
        Returns:
            The data from the front of the queue
        
        Raises:
            IndexError: If queue is empty
        
        Hint: This is different from stack! We remove from head, not tail.
        """
        # YOUR IMPLEMENTATION HERE
        pass
    
    def front(self):
        """
        View front item without removing it
        
        Returns:
            The data from the front item
        
        Hint: Similar to stack peek, but we look at head instead of tail
        """
        # YOUR IMPLEMENTATION HERE
        pass
    
    def rear(self):
        """
        View rear item without removing it
        
        Returns:
            The data from the rear item
        
        Hint: This is like stack peek - look at tail!
        """
        # YOUR IMPLEMENTATION HERE
        pass
    
    def size(self):
        """Get number of items in queue"""
        return self.size_count

# Test your queue implementation
def test_queue():
    """Test function to verify your Queue implementation"""
    print("=== Testing Queue Implementation ===\n")
    
    queue = Queue()
    print(f"Is empty? {queue.is_empty()}")
    
    # Test enqueue
    print("\n1. Testing enqueue:")
    queue.enqueue("first")
    queue.enqueue("second") 
    queue.enqueue("third")
    
    print(f"Queue size: {queue.size()}")
    print(f"Front item: {queue.front()}")
    print(f"Rear item: {queue.rear()}")
    
    # Test dequeue
    print("\n2. Testing dequeue (FIFO order):")
    while not queue.is_empty():
        item = queue.dequeue()
        print(f"Queue size now: {queue.size()}")
    
    # Test edge cases
    print("\n3. Testing edge cases:")
    try:
        queue.dequeue()  # Should raise error
    except IndexError as e:
        print(f"Correctly caught error: {e}")
    
    print("\nTest completed!")

# Uncomment to test your implementation
# test_queue()
```

### Implementation Hints

Connect this to the stack concepts you just learned:

1. **enqueue()**: Almost identical to stack push - add to tail and update pointers
2. **dequeue()**: Different from stack pop - remove from head (front) instead of tail
3. **front()**: Like stack peek, but look at head instead of tail  
4. **rear()**: Exactly like stack peek - look at tail
5. **Edge cases**: Handle empty queue just like you did for empty stack

### Key Learning Points

- **Head pointer**: Points to the front (next item to be removed)
- **Tail pointer**: Points to the rear (last item added)
- **Enqueue operation**: O(1) - just update tail pointer like stack push
- **Dequeue operation**: O(1) - just update head pointer (much better than stack pop!)
- **No traversal needed**: Unlike stack pop which needs O(n) traversal, queue operations are both O(1)
- **Perfect linked list application**: Demonstrates efficient insertions and deletions at different ends

---



## Bonus Challenge: Balanced Parentheses Checker

If you finish early, try implementing this classic stack problem:

```python
def is_balanced_parentheses(expression):
    """
    Check if parentheses, brackets, and braces are balanced
    
    Args:
        expression: String to check
    
    Returns:
        True if balanced, False otherwise
    
    Examples:
        is_balanced_parentheses("()") -> True
        is_balanced_parentheses("([{}])") -> True
        is_balanced_parentheses("([)]") -> False
    """
    stack = Stack()
    
    # YOUR IMPLEMENTATION HERE
    pass

# Test cases
test_expressions = [
    "()",           # True
    "([{}])",       # True  
    "([)]",         # False
    "(((",          # False
    ")))",          # False
    "",             # True
]

for expr in test_expressions:
    result = is_balanced_parentheses(expr)
    print(f"'{expr}' -> {result}")
```

---
