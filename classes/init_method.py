# Example 1: __init__ with one parameter
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name} says Woof!")
dog = Dog("Max")
dog.bark()

# Example 2: __init__ with two parameters
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
rect = Rectangle(4, 5)
print(rect.area())  # 20

# Example 3: __init__ with default value
class Greeter:
    def __init__(self, name, greeting="Hello"):
        self.name = name
        self.greeting = greeting
    def say_hi(self):
        print(f"{self.greeting}, {self.name}!")
g1 = Greeter("Alice")
g1.say_hi()  # Hello, Alice!

# Example 4: __init__ that stores a list
class ShoppingList:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
sl = ShoppingList()
sl.add("milk")
sl.add("bread")
print(sl.items)
