# A regular function
def square(x):
    return x * x


# The exact same functionality using lambda
square_lambda = lambda x : x*x


print(square_lambda(5))  # Output: 25

#  Map

numbers = [1, 2, 3, 4]

# Double every number using map and lambda
doubled = list(map(lambda x: x * 2, numbers))

print(doubled)  # Output: [2, 4, 6, 8]


#  Filter
numbers = [1, 2, 3, 4, 5, 6]

# Keep only the even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)  # Output: [2, 4, 6]
