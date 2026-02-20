
# Example 1: Double each number in a list
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]


# Example 2: Convert numbers to strings
nums = [1, 2, 3]
strings = list(map(lambda x: str(x), nums))
print(strings)  # ['1', '2', '3']


# Example 3: Add 10 to each number
values = [5, 10, 15]
result = list(map(lambda x: x + 10, values))
print(result)  # [15, 20, 25]


# Example 4: Get length of each word
words = ["cat", "dog", "bird"]
lengths = list(map(lambda w: len(w), words))
print(lengths)  # [3, 3, 4]
