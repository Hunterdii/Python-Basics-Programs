## 🧱 **Python Program: Implementing Stack and Queue**

### **Problem Statement:**

Write a Python program to implement **Stack** and **Queue** data structures using lists.
Both should support basic operations like insertion, deletion, and display.

---

### **Program:**

```python
# Program: Implementation of Stack and Queue in Python

# Stack Implementation (LIFO)
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            print(f"Popped: {self.stack.pop()}")
        else:
            print("Stack is empty!")

    def peek(self):
        if not self.is_empty():
            print(f"Top Element: {self.stack[-1]}")
        else:
            print("Stack is empty!")

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)


# Queue Implementation (FIFO)
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.is_empty():
            print(f"Dequeued: {self.queue.pop(0)}")
        else:
            print("Queue is empty!")

    def front(self):
        if not self.is_empty():
            print(f"Front Element: {self.queue[0]}")
        else:
            print("Queue is empty!")

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue:", self.queue)


# Main Program
if __name__ == "__main__":
    print("Stack Operations:")
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()
    s.pop()
    s.peek()
    s.display()

    print("\nQueue Operations:")
    q = Queue()
    q.enqueue(5)
    q.enqueue(15)
    q.enqueue(25)
    q.display()
    q.dequeue()
    q.front()
    q.display()
```

---

### **Explanation of Code:**

1. **Stack Implementation (LIFO - Last In First Out):**

   * `push(item)` → Adds an element to the stack.
   * `pop()` → Removes the topmost element.
   * `peek()` → Returns the topmost element without removing it.
   * `is_empty()` → Checks if the stack is empty.
   * `display()` → Prints all elements of the stack.

2. **Queue Implementation (FIFO - First In First Out):**

   * `enqueue(item)` → Adds an element to the queue.
   * `dequeue()` → Removes the front element.
   * `front()` → Displays the front element.
   * `is_empty()` → Checks if the queue is empty.
   * `display()` → Displays all elements in the queue.

3. **Main Program:**

   * Demonstrates stack and queue operations step by step.

---

### **Sample Output:**

```
Stack Operations:
Pushed: 10
Pushed: 20
Pushed: 30
Stack: [10, 20, 30]
Popped: 30
Top Element: 20
Stack: [10, 20]

Queue Operations:
Enqueued: 5
Enqueued: 15
Enqueued: 25
Queue: [5, 15, 25]
Dequeued: 5
Front Element: 15
Queue: [15, 25]
```

---

### **Summary:**

* **Stack** follows the **LIFO** principle — last element added is the first removed.
* **Queue** follows the **FIFO** principle — first element added is the first removed.
* Both are implemented using Python lists and demonstrate essential data structure operations.


