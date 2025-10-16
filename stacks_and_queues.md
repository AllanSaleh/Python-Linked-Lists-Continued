![Stack vs Queue](https://dnycf48t040dh.cloudfront.net/fit-in/840x473/stack-vs-queue.jpeg)

# 🧠 Why Stacks and Queues?

Linked Lists showed us how to connect items in order, but sometimes we need to control the order in which we access or process items. That’s where **Stacks** and **Queues** come in.

![Queue Operations](https://devopedia.org/images/article/398/2692.1643415214.png)
---

## 1️⃣ Stacks: “Last In, First Out” (LIFO)

Think of a stack of plates 🍽️:

- You add a plate on top.
- You remove the top plate first.
- The **last item** you added is the **first one** you take out.

**Useful when you need to reverse things or undo operations.**

**Real-World Use Cases:**

- Undo feature in text editors (last action is undone first)
- Browser “back” button (last page visited is first to go back to)
- Function call stack in programming (last function called is the first to return)

![Stacks](https://static-assets.codecademy.com/python-stack-data-structure/common-examples-of-stack.png)
---

## 2️⃣ Queues: “First In, First Out” (FIFO)

Think of a line at a bank or a ticket counter 🎫:

- First person to arrive is the first served.
- People join at the **end of the line** and leave from the **front**.
- The **first item added** is the **first one removed**.

**Useful when order matters and you want fairness.**

**Real-World Use Cases:**

- Print job queues (first document sent to printer prints first)
- Customer service systems (tickets are handled in order)
- CPU task scheduling (tasks processed in the order they arrive)

![Queue](https://images.shiksha.com/mediadata/ugcDocuments/images/wordpressImages/2022_08_image-190.jpg)
---

## 🔁 Bridging from Linked Lists

Remember how we used Linked Lists to store songs in a playlist?  
We can use Linked Lists as the underlying structure for Stacks and Queues:

- **Stack:** Always add/remove at the **head** (top of stack)
- **Queue:** Add at the **tail**, remove at the **head** (first in, first out)

This is great because Linked Lists allow us to add and remove nodes efficiently **without shifting everything** like in a Python list.

![Deque Operation](https://media.geeksforgeeks.org/wp-content/uploads/20250829162608668808/Dequeue-Operation-in-Queue-2.webp)
