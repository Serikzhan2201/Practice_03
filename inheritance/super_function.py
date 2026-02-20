# Example 1: super() to call parent __init__
class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent init
        self.breed = breed
dog = Dog("Max", "Labrador")
print(dog.name, dog.breed)  # Max Labrador

# Example 2: super() to call parent method
class Greeter:
    def greet(self):
        return "Hello"
class LoudGreeter(Greeter):
    def greet(self):
        msg = super().greet()  # Get parent's greeting
        return msg.upper()     # Make it loud
g = LoudGreeter()
print(g.greet())  # HELLO

# Example 3: super() with extra setup in child
class Shape:
    def __init__(self, color):
        self.color = color
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
c = Circle("blue", 5)
print(c.color, c.radius)  # blue 5

# Example 4: super() to extend parent behavior
class Base:
    def show(self):
        print("Base")
class Child(Base):
    def show(self):
        super().show()  # Call parent first
        print("Child")  # Then add more
obj = Child()
obj.show()  # Base then Child
