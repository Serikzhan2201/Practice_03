# Example 1: Class variable - shared count
class Dog:
    count = 0  # Class variable
    def __init__(self, name):
        self.name = name  # Instance variable
        Dog.count += 1
d1 = Dog("Max")
d2 = Dog("Bella")
print(Dog.count)  # 2

# Example 2: Class variable as a constant
class Circle:
    pi = 3.14159  # Shared constant
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return Circle.pi * self.radius ** 2
c = Circle(5)
print(c.area())  # 78.54...

# Example 3: Class variable for species
class Animal:
    species = "unknown"
    def __init__(self, name):
        self.name = name
a1 = Animal("Rex")
a2 = Animal("Luna")
print(a1.species)  # unknown (same for all)
print(a2.species)  # unknown

# Example 4: Accessing class variable from instance
class Car:
    wheels = 4
    def __init__(self, color):
        self.color = color
    def info(self):
        print(f"Color: {self.color}, Wheels: {Car.wheels}")
car = Car("red")
car.info()  # Color: red, Wheels: 4
