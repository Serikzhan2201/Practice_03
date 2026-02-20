# Example 1: *args - accept any number of arguments as a tuple
def add_all(*numbers):
    total = sum(numbers)
    print(f"Sum: {total}")
add_all(1, 2, 3)
add_all(5, 10, 15, 20)

# Example 2: *args - print all arguments
def print_all(*items):
    for item in items:
        print(item, end=" ")
    print()
print_all("apple", "banana", "cherry")

# Example 3: **kwargs - accept any number of keyword arguments as a dict
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=25, city="Paris")

# Example 4: Mix of normal, *args, and **kwargs
def show_details(title, *items, **options):
    print(f"Title: {title}")
    print("Items:", items)
    print("Options:", options)
show_details("Shopping", "apple", "milk", color="red", size="large")
