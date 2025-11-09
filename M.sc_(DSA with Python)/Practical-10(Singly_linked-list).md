## 🔗 **Python Program: Implementation of Singly Linked List**

### **Problem Statement:**

Write a Python program to implement a **Singly Linked List** supporting the following operations:

* Insertion at end
* Deletion by value
* Display of list elements

---

### **Program:**

```python
# Program: Implementation of Singly Linked List

# Node class representing each element
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the end
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Delete a node by value
    def delete(self, key):
        temp = self.head

        # If head node holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if not temp:
            print(f"Value {key} not found in list.")
            return

        prev.next = temp.next
        temp = None

    # Display the linked list
    def display(self):
        temp = self.head
        if not temp:
            print("List is empty.")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Main Program
if __name__ == "__main__":
    llist = LinkedList()
    llist.insert(10)
    llist.insert(20)
    llist.insert(30)
    print("Linked List after insertion:")
    llist.display()

    llist.delete(20)
    print("\nLinked List after deleting 20:")
    llist.display()

    llist.delete(50)  # Attempt to delete non-existing element
```

---

### **Explanation of Code:**

1. **Node Class:**

   * Represents a single node in the linked list.
   * Each node has:

     * `data` → value stored in the node.
     * `next` → pointer to the next node.

2. **LinkedList Class:**

   * Manages all nodes using `head` as the starting point.
   * **`insert(data)`** → Adds a new node at the end.
   * **`delete(key)`** → Removes a node that matches the given value.
   * **`display()`** → Traverses and prints all nodes.

3. **Main Program:**

   * Demonstrates list creation, insertion, deletion, and display operations.

---

### **Sample Output:**

```
Linked List after insertion:
10 -> 20 -> 30 -> None

Linked List after deleting 20:
10 -> 30 -> None
Value 50 not found in list.
```

---

### **Summary:**

* **Singly Linked List** is a linear data structure consisting of nodes linked sequentially.
* Each node stores data and a pointer to the next node.
* Operations implemented:

  * **Insertion at end**
  * **Deletion by value**
  * **Traversal/Display**
* Efficient for dynamic memory management and insertion/deletion operations compared to arrays.