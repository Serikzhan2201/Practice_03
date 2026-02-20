
# Example 1: Sort list of tuples by second element
pairs = [(1, 5), (2, 3), (3, 8)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # [(2, 3), (1, 5), (3, 8)]


# Example 2: Sort words by length
words = ["apple", "pie", "banana", "a"]
by_length = sorted(words, key=lambda w: len(w))
print(by_length)  # ['a', 'pie', 'apple', 'banana']


# Example 3: Sort numbers by absolute value (ignore negative sign)
numbers = [-5, 2, -1, 8, -3]
by_abs = sorted(numbers, key=lambda x: abs(x))
print(by_abs)  # [-1, 2, -3, -5, 8]


# Example 4: Sort list of names by last character
names = ["Anna", "Bob", "Chris", "Diana"]
by_last = sorted(names, key=lambda n: n[-1])
print(by_last)  # ['Diana', 'Bob', 'Anna', 'Chris']
