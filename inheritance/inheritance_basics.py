# Example 1: Child inherits method from parent
class Animal:
    def speak(self):
        print("Some sound")
class Dog(Animal):
    pass  # Dog has speak() from Animal
dog = Dog()
dog.speak()  # Some sound

# Example 2: Child adds its own method
class Bird(Animal):
    def fly(self):
        print("Flying!")
bird = Bird()
bird.speak()  # From Animal
bird.fly()    # From Bird

# Example 3: Child inherits __init__ from parent
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hi, I'm {self.name}")
class Student(Person):
    pass
s = Student("Alice")
s.greet()  # Hi, I'm Alice

# Example 4: Child has both parent's and own attributes
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels
class Car(Vehicle):
    def __init__(self, wheels, color):
        Vehicle.__init__(self, wheels)  # Call parent init
        self.color = color
car = Car(4, "red")
print(car.wheels, car.color)  # 4 red
