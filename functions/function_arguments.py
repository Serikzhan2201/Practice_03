# Example 1: Positional arguments - order matters
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")
describe_pet("dog", "Max")

# Example 2: Keyword arguments - order doesn't matter
def greet(greeting, name):
    print(f"{greeting}, {name}!")
greet(name="Bob", greeting="Hey")

# Example 3: Default argument - has a fallback value
def greet_person(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
greet_person("Alice")  # Uses default "Hello"
greet_person("Bob", "Hi")  # Overrides with "Hi"

# Example 4: Mix of positional and default arguments
def make_coffee(size="medium", sugar=1):
    print(f"Coffee: {size} size, {sugar} sugar(s)")
make_coffee()
make_coffee("large")
make_coffee("small", 2)
