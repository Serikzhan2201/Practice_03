# Example 1: Override a method completely
class Animal:
    def speak(self):
        print("Some sound")
class Cat(Animal):
    def speak(self):  # Override - replace parent's speak
        print("Meow!")
cat = Cat()
cat.speak()  # Meow! (not "Some sound")

# Example 2: Override with different logic
class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):  # Override with real calculation
        return self.side * self.side
sq = Square(4)
print(sq.area())  # 16

# Example 3: Override __init__
class Person:
    def __init__(self, name):
        self.name = name
class Employee(Person):
    def __init__(self, name, job):  # Override init, add job
        super().__init__(name)
        self.job = job
emp = Employee("Bob", "Teacher")
print(emp.name, emp.job)  # Bob Teacher

# Example 4: Override with different return type
class Printer:
    def get_message(self):
        return "Printing..."
class BoldPrinter(Printer):
    def get_message(self):  # Override - return different format
        return "** PRINTING **"
p = BoldPrinter()
print(p.get_message())  # ** PRINTING **
