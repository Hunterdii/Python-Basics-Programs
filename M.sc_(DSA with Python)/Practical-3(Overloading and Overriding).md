## ⚙️ **Problem: Method Overloading and Overriding in Python**

### 📝 **Problem Description**

This program demonstrates two major OOP concepts in Python:

1. **Method Overloading (Simulated)** → Same method name with different argument patterns (not truly supported in Python, only simulated using default parameters or variable-length arguments).
2. **Method Overriding** → Subclass provides its own implementation of a parent class method (fully supported in Python, enabling runtime polymorphism).

---

## 💻 **Program 1: Combined Demonstration of Method Overloading and Overriding**

```python
# ⚙️ Combined Program: Method Overloading and Overriding in Python

# ----- Method Overloading (Simulated) -----
class Calculator:
    """Class demonstrating simulated method overloading using default arguments."""
    def add(self, a=0, b=0, c=0):
        """Simulates method overloading by using default parameters."""
        return a + b + c


# ----- Method Overriding -----
class Animal:
    """Parent class representing generic animals."""
    def sound(self):
        print("Animals make different sounds")


class Dog(Animal):
    """Subclass overriding the sound() method."""
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    """Subclass overriding the sound() method."""
    def sound(self):
        print("Cat meows")


# ----- Main Program -----
if __name__ == "__main__":
    print("🧮 Demonstration: Method Overloading and Overriding\n")

    # --- Method Overloading Example ---
    calc = Calculator()
    print("🔹 Method Overloading (Simulated in Python)")
    print("One argument:", calc.add(5))            # 5
    print("Two arguments:", calc.add(5, 10))       # 15
    print("Three arguments:", calc.add(5, 10, 20)) # 35

    # --- Method Overriding Example ---
    print("\n🐾 Method Overriding (Runtime Polymorphism)")
    a = Animal()
    d = Dog()
    c = Cat()

    a.sound()  # Calls Animal's version
    d.sound()  # Calls Dog's version
    c.sound()  # Calls Cat's version
```

---

### 📊 **Sample Output**

```
🧮 Demonstration: Method Overloading and Overriding

🔹 Method Overloading (Simulated in Python)
One argument: 5
Two arguments: 15
Three arguments: 35

🐾 Method Overriding (Runtime Polymorphism)
Animals make different sounds
Dog barks
Cat meows
```

---

### 🧠 **Explanation of Combined Code**

* The **`Calculator`** class simulates **method overloading** using default arguments in `add()`.
* The **`Animal`**, **`Dog`**, and **`Cat`** classes demonstrate **method overriding**, where subclasses redefine the parent’s method `sound()`.
* Together, these show **compile-time-like polymorphism (simulated)** and **runtime polymorphism (real)** in Python.

---

## 💻 **Program 2: Method Overloading (Simulated)**

```python
# 🧮 Program: Method Overloading (Simulated in Python)

class Calculator:
    # Method with default arguments to simulate overloading
    def add(self, a=0, b=0, c=0):
        return a + b + c


# Object creation
calc = Calculator()

# Different ways of calling 'add'
print('One argument:', calc.add(5))           # 5
print('Two arguments:', calc.add(5, 10))      # 15
print('Three arguments:', calc.add(5, 10, 20))# 35
```

---

### 🧩 **Explanation**

* The class `Calculator` contains one method `add()` with default parameter values.
* Depending on the number of arguments passed:

  * `calc.add(5)` → returns 5
  * `calc.add(5,10)` → returns 15
  * `calc.add(5,10,20)` → returns 35
* Thus, a single method handles multiple argument counts — **simulating overloading**.

---

### 📊 **Output**

```
One argument: 5
Two arguments: 15
Three arguments: 35
```

---

## 💻 **Program 3: Method Overriding**

```python
# 🐾 Program: Method Overriding in Python

class Animal:
    def sound(self):
        print('Animals make different sounds')


class Dog(Animal):
    def sound(self):  # Overriding parent method
        print('Dog barks')


class Cat(Animal):
    def sound(self):  # Overriding parent method
        print('Cat meows')


# Object creation
a = Animal()
d = Dog()
c = Cat()

# Method calls
a.sound()  # Calls Animal's version
d.sound()  # Calls Dog's overridden version
c.sound()  # Calls Cat's overridden version
```

---

### 🧩 **Explanation**

* The **parent class** `Animal` defines a generic method `sound()`.
* **Subclasses** `Dog` and `Cat` override this method with their own implementations.
* The method call result depends on the object type (not the reference), demonstrating **runtime polymorphism**.

---

### 📊 **Output**

```
Animals make different sounds
Dog barks
Cat meows
```

---

## 🧾 **Summary**

| Feature               | Method Overloading                                           | Method Overriding                        |
| --------------------- | ------------------------------------------------------------ | ---------------------------------------- |
| **Definition**        | Same method name with different parameters                   | Same method name redefined in subclass   |
| **Support in Python** | Simulated only (default args / *args / **kwargs)             | Fully supported                          |
| **Binding Type**      | Compile-time (in other languages), simulated here            | Runtime (dynamic binding)                |
| **Purpose**           | Flexibility in calling method with different argument counts | Specialized behavior in subclasses       |
| **Example**           | `calc.add(5,10,20)`                                          | `Dog.sound()` overrides `Animal.sound()` |

