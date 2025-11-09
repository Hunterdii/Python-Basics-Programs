## 🌸 **Problem: Class Implementation – Flower Details using OOP in Python**

### 📝 **Problem Description**

Create a Python program that defines a class `Flower` to represent a flower’s details — its **name**, **number of petals**, and **price**.

The class should:

* Have **three instance variables**:

  * `name` (string): the name of the flower
  * `petals` (integer): the number of petals
  * `price` (float): the price of the flower
* Include a **constructor** (`__init__`) to initialize these attributes.
* Provide **setter methods** to update the values of each attribute.
* Provide **getter methods** to retrieve the values of each attribute.
* Demonstrate the class functionality by creating a `Flower` object, displaying its details, modifying its attributes, and printing the updated values.

---

### 💻 **Python Program**

```python
# 🌸 Program: Class Implementation - Flower Details using OOP

class Flower:
    """A class to represent a flower with name, number of petals, and price."""

    def __init__(self, name: str, petals: int, price: float):
        """Constructor to initialize the flower's name, petals, and price."""
        self.name = name
        self.petals = petals
        self.price = price

    # Setter methods
    def set_name(self, name: str):
        """Set a new name for the flower."""
        self.name = name

    def set_petals(self, petals: int):
        """Set a new number of petals for the flower."""
        self.petals = petals

    def set_price(self, price: float):
        """Set a new price for the flower."""
        self.price = price

    # Getter methods
    def get_name(self) -> str:
        """Return the flower's name."""
        return self.name

    def get_petals(self) -> int:
        """Return the number of petals."""
        return self.petals

    def get_price(self) -> float:
        """Return the flower's price."""
        return self.price


# Main program execution
if __name__ == "__main__":
    # Creating a Flower object
    my_flower = Flower("Rose", 32, 10.5)

    # Displaying initial details
    print("🌺 Flower Details:")
    print("Name:", my_flower.get_name())
    print("Number of Petals:", my_flower.get_petals())
    print("Price:", my_flower.get_price())

    # Modifying the flower details using setter methods
    my_flower.set_name("Lily")
    my_flower.set_petals(6)
    my_flower.set_price(7.25)

    # Displaying updated details
    print("\n🌼 Updated Flower Details:")
    print("Name:", my_flower.get_name())
    print("Number of Petals:", my_flower.get_petals())
    print("Price:", my_flower.get_price())
```

---

### 🧠 **Explanation of the Code**

1. **Class Definition**
   `class Flower:`
   Defines a new class named `Flower` that encapsulates attributes and behaviors related to a flower.

2. **Constructor (`__init__` Method)**
   Initializes the object with:

   * `name`: Name of the flower (string)
   * `petals`: Number of petals (integer)
   * `price`: Price of the flower (float)

3. **Setter Methods**
   Allow modification of the private attributes:

   * `set_name()` → Updates the flower’s name
   * `set_petals()` → Updates the number of petals
   * `set_price()` → Updates the price

4. **Getter Methods**
   Provide access to the attributes:

   * `get_name()` → Returns the name
   * `get_petals()` → Returns the number of petals
   * `get_price()` → Returns the price

5. **Main Block (`if __name__ == "__main__":`)**
   Ensures the test code runs only when executed directly (not on import).
   Demonstrates:

   * Object creation (`Flower("Rose", 32, 10.5)`)
   * Accessing and printing initial data
   * Modifying attributes with setters
   * Printing updated flower details

---

### 📊 **Output**

```
🌺 Flower Details:
Name: Rose
Number of Petals: 32
Price: 10.5

🌼 Updated Flower Details:
Name: Lily
Number of Petals: 6
Price: 7.25
```