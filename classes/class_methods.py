# Example 1: Instance method - uses self
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
calc = Calculator()
print(calc.add(5, 3))      # 8
print(calc.subtract(5, 3)) # 2

# Example 2: Method that uses instance data
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print(f"Balance: ${self.balance}")
account = BankAccount(100)
account.deposit(50)
account.show_balance()  # Balance: $150

# Example 3: Method that returns a value
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    def to_fahrenheit(self):
        return self.celsius * 9/5 + 32
temp = Temperature(25)
print(temp.to_fahrenheit())  # 77.0

# Example 4: Multiple methods working together
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def reset(self):
        self.count = 0
    def get_count(self):
        return self.count
c = Counter()
c.increment()
c.increment()
print(c.get_count())  # 2
