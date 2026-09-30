# Sorting a list
numbers = [4, 2, 8, 5]
new_numbers = sorted(numbers)
print(new_numbers)  # Output: [2, 4, 5, 8]
print(numbers)      # Output: [4, 2, 8, 5] (Original is intact)

# Sorting a string (returns a list of characters)
print(sorted("python"))  # Output: ['h', 'n', 'o', 'p', 't', 'y']

numbers = [4, 2, 8, 5]
numbers.sort()
print(numbers)  # Output: [2, 4, 5, 8] (Original list is changed)


nums = [1, 5, 3, 9]
print(sorted(nums, reverse=True))  # Output: [9, 5, 3, 1]

#  custom sort
words = ["banana", "fig", "watermelon", "apple"]
# Sorts shortest to longest
print(sorted(words, key=len))
# Output: ['fig', 'apple', 'banana', 'watermelon']

students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
# Sort by age (the second element of the tuple, index 1)
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)
# Output: [('Bob', 20), ('Charlie', 23), ('Alice', 25)]
