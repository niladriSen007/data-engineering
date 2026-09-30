fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

#  changing the start index
fruits = ["apple", "banana", "cherry"]

for count, fruit in enumerate(fruits, start=1):
    print(f"Item {count}: {fruit}")

# Converting directly to a List of Tuples
fruits = ["apple", "banana", "cherry"]

pairs_list = list(enumerate(fruits, start=10))
print(pairs_list)
