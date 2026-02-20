# Example 1: Child inherits from two parents
class Flyer:
    def fly(self):
        print("Flying!")
class Swimmer:
    def swim(self):
        print("Swimming!")
class Duck(Flyer, Swimmer):  # Inherits from both
    pass
duck = Duck()
duck.fly()   # From Flyer
duck.swim()  # From Swimmer

# Example 2: Child adds its own method
class Walker:
    def walk(self):
        print("Walking")
class Runner:
    def run(self):
        print("Running")
class Athlete(Walker, Runner):
    def jump(self):
        print("Jumping")
a = Athlete()
a.walk()
a.run()
a.jump()

# Example 3: Both parents have same method - first parent wins
class A:
    def greet(self):
        print("A says hi")
class B:
    def greet(self):
        print("B says hi")
class C(A, B):  # A comes first, so A's greet is used
    pass
obj = C()
obj.greet()  # A says hi

# Example 4: Multiple inheritance with __init__
class Named:
    def __init__(self, name):
        self.name = name
class Aged:
    def __init__(self, age):
        self.age = age
class Person(Named, Aged):
    def __init__(self, name, age):
        Named.__init__(self, name)
        Aged.__init__(self, age)
p = Person("Alice", 25)
print(p.name, p.age)  # Alice 25
