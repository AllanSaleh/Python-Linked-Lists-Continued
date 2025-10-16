# Linked Lists

Linked List is a chain of nodes, where each node stores some data and a reference (link) to the next node in the chain.

These lists are dependant on keeping track of what it considered to be the "head" and "tail". (the head is absolutely necessary, and the tail is convenient especially when treating the list as a stack)

- **Head**: The head is the starting point of the list, the one that initiates the chain reaction of finding what comes nexts. As long as you know where the head of the list is, you can find every other element.

- **Tail**: Conversely, the tail is the end of the chain, and keeping track of it, can make adding/appending new items to the chain much easier.

#### Singly Linked Lists:
Singly Linked lists are a one way street, and can only travel down the "next" stream with no way of getting back. Singly linked lists realy on tracking the "Head" even more so because of this.

![Linked-list-image](https://media.geeksforgeeks.org/wp-content/uploads/singly-linkedlist.png)

---

## 🧠 Why not just use a normal Python list?

A Python list (`[]`) and a Linked List both store collections of data — but they work very differently under the hood.

| Feature | Python List | Linked List |
|---------|------------|-------------|
| **Memory Layout** | Stored in one continuous block of memory | Scattered in memory — each node points to the next |
| **Accessing elements** | Fast! You can access any element by index (e.g., `my_list[3]`) | Slower — must start at the head and follow links until you reach that position |
| **Inserting or deleting in the middle** | Expensive — shifts all later elements | Easy — just change a couple of links |
| **Best for** | When you need fast random access | When you insert/remove often and don’t need indexes |

---

## ⚙️ When are Linked Lists used in real life?

Linked Lists are used under the hood in many data structures and systems:

- **Music playlists** – each song links to the next.  
- **Undo/Redo functionality** – each action links to the previous one.  
- **Navigating browser history** – "back" and "forward" buttons rely on linked nodes.  
- **Operating systems and memory management** – to efficiently store and remove items without shifting large blocks of data.
