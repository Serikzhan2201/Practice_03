# Example 1: Return a single value
def get_full_name(first, last):
    return f"{first} {last}"
name = get_full_name("John", "Doe")
print(name)

# Example 2: Return a number (sum)
def sum_numbers(a, b):
    return a + b
total = sum_numbers(10, 20)
print(total)

# Example 3: Return True or False (boolean)
def is_even(number):
    return number % 2 == 0
print(is_even(4))  # True
print(is_even(7))  # False

# Example 4: Return a list
def get_first_three():
    return [1, 2, 3]
numbers = get_first_three()
print(numbers)
