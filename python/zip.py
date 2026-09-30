from itertools import zip_longest
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# Combine lists
zipped = zip(names, scores)

# Convert to a list to view the contents
print(list(zipped))
# Output: [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")


letters = ['A', 'B']
numbers = [1, 2, 3, 4]

# 1. Default (Truncates)
print(list(zip(letters, numbers)))          # [('A', 1), ('B', 2)]

# 2. Strict Mode (Raises ValueError)
# print(list(zip(letters, numbers, strict=True)))

# 3. Zip Longest (Fills gaps)
print(list(zip_longest(letters, numbers, fillvalue="😊")))
# [('A', 1), ('B', 2), ('?', 3), ('?', 4)]

keys = ["a", "b", "c"]
values = [1, 2, 3]
my_dict = dict(zip(keys, values))  # {'a': 1, 'b': 2, 'c': 3}


pairs = [('Alice', 85), ('Bob', 92)]
names, scores = zip(*pairs)

print(names)  # ('Alice', 'Bob')
print(scores)  # (85, 92)
