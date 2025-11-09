## 🎯 **Python Program: Generate Combinations of n Distinct Objects**

### **Problem Statement:**

Write a Python program to generate all possible combinations of **n distinct objects** taken from the elements of a given list.

**Example:**
Original list: `[1, 2, 3, 4, 5, 6, 7, 8, 9]`
Combinations of 2 distinct objects: `[1, 2] [1, 3] [1, 4] ... [7, 8] [7, 9] [8, 9]`

---

### **Program:**

```python
# Program: Generate Combinations of n Distinct Objects

# Function to generate combinations manually using backtracking
def generate_combinations(lst, n):
    result = []

    def backtrack(start, path):
        # If the combination has n elements, add to result
        if len(path) == n:
            result.append(path[:])
            return

        # Explore further elements
        for i in range(start, len(lst)):
            path.append(lst[i])
            backtrack(i + 1, path)
            path.pop()  # Backtrack to explore new possibilities

    backtrack(0, [])
    return result


# Example usage
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 2
result = generate_combinations(original_list, n)

# Displaying the results
print(f"Original list: {original_list}")
print(f"Combinations of {n} distinct objects:")
for combo in result:
    print(combo, end=" ")
```

---

### **Step-by-Step Explanation of Code:**

#### **1. Function Definition**

```python
def generate_combinations(lst, n):
    result = []
```

* **`lst`** → the list of elements (e.g., `[1,2,3,4,5,6,7,8,9]`).
* **`n`** → number of elements in each combination.
* **`result`** → an empty list that will store all generated combinations.

---

#### **2. Backtracking Helper Function**

```python
def backtrack(start, path):
```

* **`start`** → current index in the list from where to pick elements next.
* **`path`** → temporary list storing the current combination being built.

This recursive function builds combinations step-by-step.

---

#### **3. Base Case**

```python
if len(path) == n:
    result.append(path[:])
    return
```

* When the current combination **has n elements**, it is added to the result.
* `path[:]` makes a **copy** of the list to prevent later modification.

---

#### **4. Recursive Exploration**

```python
for i in range(start, len(lst)):
    path.append(lst[i])       # Choose the element
    backtrack(i + 1, path)    # Explore further
    path.pop()                # Undo the choice (backtrack)
```

* Iterates through remaining elements starting from index `start`.
* Adds each element to the current path, explores deeper, and removes it afterward.
* Ensures:

  * **No repetition** of elements.
  * **Order doesn’t matter** → `[1, 2]` and `[2, 1]` are treated as the same combination.

---

#### **5. Initial Call**

```python
backtrack(0, [])
```

* Starts from index 0 with an **empty path**.
* Triggers recursive exploration to generate all valid combinations.

---

#### **6. Final Output**

```python
return result
```

* After all recursive calls finish, the `result` list contains every possible combination of length `n`.

---

### **Sample Output:**

```
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Combinations of 2 distinct objects:
[1, 2] [1, 3] [1, 4] [1, 5] [1, 6] [1, 7] [1, 8] [1, 9]
[2, 3] [2, 4] [2, 5] [2, 6] [2, 7] [2, 8] [2, 9]
[3, 4] [3, 5] [3, 6] [3, 7] [3, 8] [3, 9]
[4, 5] [4, 6] [4, 7] [4, 8] [4, 9]
[5, 6] [5, 7] [5, 8] [5, 9]
[6, 7] [6, 8] [6, 9]
[7, 8] [7, 9]
[8, 9]
```

---

### **Summary:**

* The program uses **backtracking** to generate all unique combinations.
* It avoids repetition and ensures each combination contains exactly **n** elements.
* This approach can be easily extended to handle larger lists or different combination sizes.

---

### **Alternative Approach (Using itertools):**

```python
from itertools import combinations

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 2
result = list(combinations(lst, n))
print(result)
```

✅ **`itertools.combinations()`** automatically handles all combination logic efficiently — perfect for concise or production-grade code.
