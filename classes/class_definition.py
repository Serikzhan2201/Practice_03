# Example 1: Empty class (placeholder)
class EmptyClass:
    pass
obj1 = EmptyClass()
print(obj1)

# Example 2: Simple class with one method
class Dog:
    def bark(self):
        print("Woof!")
my_dog = Dog()
my_dog.bark()

# Example 3: Class with two methods
class Cat:
    def meow(self):
        print("Meow!")
    def sleep(self):
        print("Zzz...")
my_cat = Cat()
my_cat.meow()
my_cat.sleep()

# Example 4: Class with attribute assigned after creation
class Person:
    def greet(self):
        print(f"Hi, I am {self.name}")
p = Person()
p.name = "Alice"
p.greet()
