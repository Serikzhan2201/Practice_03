
# Example 1: Filter even numbers only
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]


# Example 2: Filter numbers greater than 5
nums = [3, 7, 2, 9, 4]
big = list(filter(lambda x: x > 5, nums))
print(big)  # [7, 9]


# Example 3: Filter non-empty strings
words = ["hello", "", "world", "", "!"]
non_empty = list(filter(lambda s: len(s) > 0, words))
print(non_empty)  # ['hello', 'world', '!']


# Example 4: Filter words longer than 3 characters
items = ["a", "abc", "abcd", "ab", "abcdef"]
long_words = list(filter(lambda w: len(w) > 3, items))
print(long_words)  # ['abcd', 'abcdef']
