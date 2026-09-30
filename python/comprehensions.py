squares = [x**2 for x in range(1, 5)]
print(squares)

squares_even = [x**2 for x in range(1, 5) if x % 2 == 0]
print(squares_even)

dictionary = {x: x**2 for x in range(1, 5)}
print(dictionary)

names = ["alice", "bob", "charlie"]
name_length = {name: len(name) for name in names}
print(name_length)

word = "mississippi"
set_comprehension = {char.upper() for char in word}
print(set_comprehension)

# advance
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print(labels)