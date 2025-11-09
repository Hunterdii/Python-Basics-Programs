## 🔷 **Problem: Polygon Inheritance Hierarchy using Abstract Base Class**

### 📝 **Problem Description**

Create an inheritance hierarchy for polygons using Object-Oriented Programming (OOP) in Python.
Define an **abstract base class `Polygon`** with abstract methods `area()` and `perimeter()`.
Implement concrete subclasses:

* `Triangle`
* `Quadrilateral` (assumed to be a rectangle)
* `Pentagon` (regular pentagon)

Each subclass should implement its own formula for **area** and **perimeter**.
Write a program that allows users to select the type of polygon, input dimensions, and display the calculated **area** and **perimeter**.

---

### 💻 **Python Program**

```python
# 🔷 Program: Polygon Inheritance Hierarchy using Abstract Base Class

from abc import ABC, abstractmethod
import math

# Abstract Base Class
class Polygon(ABC):
    """Abstract base class representing a polygon."""

    @abstractmethod
    def area(self):
        """Abstract method to compute area of polygon."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to compute perimeter of polygon."""
        pass


# 🔺 Triangle Class
class Triangle(Polygon):
    """Class representing a triangle."""

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        """Compute area using Heron's formula."""
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self) -> float:
        """Compute perimeter of triangle."""
        return self.a + self.b + self.c


# ⬜ Quadrilateral Class (Rectangle Assumed)
class Quadrilateral(Polygon):
    """Class representing a rectangle (as a special quadrilateral)."""

    def __init__(self, length: float, breadth: float):
        self.length = length
        self.breadth = breadth

    def area(self) -> float:
        """Compute area of rectangle."""
        return self.length * self.breadth

    def perimeter(self) -> float:
        """Compute perimeter of rectangle."""
        return 2 * (self.length + self.breadth)


# ⬟ Pentagon Class (Regular Pentagon)
class Pentagon(Polygon):
    """Class representing a regular pentagon."""

    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        """Compute area of regular pentagon."""
        return (1 / 4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (self.side ** 2)

    def perimeter(self) -> float:
        """Compute perimeter of pentagon."""
        return 5 * self.side


# 🧮 Main Program
if __name__ == "__main__":
    print("Choose Polygon: 1. Triangle  2. Quadrilateral  3. Pentagon")
    choice = int(input("Enter choice: "))

    if choice == 1:
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = float(input("Enter side c: "))
        t = Triangle(a, b, c)
        print("\n🔺 Triangle Details:")
        print("Area:", round(t.area(), 2))
        print("Perimeter:", t.perimeter())

    elif choice == 2:
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        q = Quadrilateral(l, b)
        print("\n⬜ Quadrilateral Details:")
        print("Area:", q.area())
        print("Perimeter:", q.perimeter())

    elif choice == 3:
        s = float(input("Enter side length: "))
        p = Pentagon(s)
        print("\n⬟ Pentagon Details:")
        print("Area:", round(p.area(), 2))
        print("Perimeter:", p.perimeter())

    else:
        print("\n❌ Invalid Choice!")
```

---

### 🧠 **Explanation of the Code**

1. **Abstract Base Class – `Polygon`**

   * Imported from Python’s `abc` module.
   * Defines two abstract methods:

     * `area()` → must compute area.
     * `perimeter()` → must compute perimeter.
   * Any subclass **must** override both methods.

2. **`Triangle` Class**

   * Inherits from `Polygon`.
   * Uses **Heron’s formula**:
     [
     \text{Area} = \sqrt{s(s-a)(s-b)(s-c)}
     ]
     where ( s = \frac{a+b+c}{2} )
   * Perimeter = `a + b + c`

3. **`Quadrilateral` Class (Rectangle Assumed)**

   * Inherits from `Polygon`.
   * Area = `length × breadth`
   * Perimeter = `2 × (length + breadth)`

4. **`Pentagon` Class (Regular Pentagon)**

   * Inherits from `Polygon`.
   * Area =
     [
     \frac{1}{4} \sqrt{5(5 + 2\sqrt{5})} \times \text{side}^2
     ]
   * Perimeter = `5 × side`

5. **Main Program**

   * Prompts user to choose a polygon.
   * Takes dimensions as input.
   * Creates the respective object.
   * Displays both **area** and **perimeter** with proper formatting.

---

### 📊 **Sample Output**

**Case 1: Triangle**

```
Choose Polygon: 1. Triangle  2. Quadrilateral  3. Pentagon
Enter choice: 1
Enter side a: 3
Enter side b: 4
Enter side c: 5

🔺 Triangle Details:
Area: 6.0
Perimeter: 12.0
```

**Case 2: Quadrilateral**

```
Choose Polygon: 1. Triangle  2. Quadrilateral  3. Pentagon
Enter choice: 2
Enter length: 5
Enter breadth: 10

⬜ Quadrilateral Details:
Area: 50.0
Perimeter: 30.0
```

**Case 3: Pentagon**

```
Choose Polygon: 1. Triangle  2. Quadrilateral  3. Pentagon
Enter choice: 3
Enter side length: 6

⬟ Pentagon Details:
Area: 61.94
Perimeter: 30.0
```
