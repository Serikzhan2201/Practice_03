# Example 1: Basic lambda - add two numbers
add = lambda x, y: x + y
print(add(3, 5))  # 8

# Example 2: Lambda with one argument - double a number
double = lambda x: x * 2
print(double(10))  # 20

# Example 3: Lambda - check if number is even
is_even = lambda n: n % 2 == 0
print(is_even(4))   # True
print(is_even(7))   # False

# Example 4: Lambda - get string length
get_length = lambda s: len(s)
print(get_length("hello"))  # 5
