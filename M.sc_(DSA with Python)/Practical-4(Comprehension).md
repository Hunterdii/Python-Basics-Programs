## 🧮 **Python Program to Illustrate Comprehensions**

### 📘 **Objective**

This program demonstrates **four types of comprehensions** in Python:

1. **List Comprehension**
2. **Dictionary Comprehension**
3. **Set Comprehension**
4. **Generator Comprehension**

Comprehensions provide a **concise and efficient** way to create collections in Python.

---

## 💻 **Program: Demonstration of List, Dictionary, Set, and Generator Comprehensions**

```python
# 🧮 Program: Illustrating Different Types of Comprehensions in Python

# ---------- a) List Comprehension ----------
# Create a list of squares of numbers from 1 to 10
list_comp = [x ** 2 for x in range(1, 11)]
print("a) List Comprehension (Squares 1–10):", list_comp)


# ---------- b) Dictionary Comprehension ----------
# Create a dictionary mapping numbers to their cubes
dict_comp = {x: x ** 3 for x in range(1, 6)}
print("b) Dictionary Comprehension (Number: Cube):", dict_comp)


# ---------- c) Set Comprehension ----------
# Create a set of even numbers from 1 to 20
set_comp = {x for x in range(1, 21) if x % 2 == 0}
print("c) Set Comprehension (Even Numbers):", set_comp)


# ---------- d) Generator Comprehension ----------
# Create a generator that yields squares of numbers
gen_comp = (x ** 2 for x in range(1, 6))
print("d) Generator Comprehension (Squares 1–5):", list(gen_comp))  # Converted to list for display
```

---

### 📊 **Sample Output**

```
a) List Comprehension (Squares 1–10): [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b) Dictionary Comprehension (Number: Cube): {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
c) Set Comprehension (Even Numbers): {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
d) Generator Comprehension (Squares 1–5): [1, 4, 9, 16, 25]
```

---

## 🧠 **Explanation**

| Type                         | Syntax                                           | Description                                       | Example Output            |
| ---------------------------- | ------------------------------------------------ | ------------------------------------------------- | ------------------------- |
| **List Comprehension**       | `[expression for item in iterable if condition]` | Creates a **list** in a single line.              | `[1, 4, 9, 16, 25, ...]`  |
| **Dictionary Comprehension** | `{key: value for item in iterable}`              | Creates a **dictionary** with key-value pairs.    | `{1:1, 2:8, 3:27, ...}`   |
| **Set Comprehension**        | `{expression for item in iterable if condition}` | Creates a **set** (unique values only).           | `{2, 4, 6, 8, ...}`       |
| **Generator Comprehension**  | `(expression for item in iterable)`              | Creates a **generator object** (lazy evaluation). | Yields values one by one. |

---

## 🧾 **Summary**

| Comprehension Type | Data Structure Created | Mutable | Returns                   |
| ------------------ | ---------------------- | ------- | ------------------------- |
| **List**           | List                   | ✅ Yes   | `[ ... ]`                 |
| **Dictionary**     | Dict                   | ✅ Yes   | `{key: value}`            |
| **Set**            | Set                    | ✅ Yes   | `{ ... }` (unique)        |
| **Generator**      | Iterator               | ❌ No    | `( ... )` (lazy sequence) |

