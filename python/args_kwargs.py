def args(*args):
    print(type(args))
    print(sum(args))


def kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)


args(1, 2)
kwargs(name="Nil", age=26)


def master_function(param1, *args, **kwargs):
    print(f"Standard param: {param1}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


master_function("Hello", 1, 2, 3, status="active", role="admin")
# Output:
# Standard param: Hello
# args: (1, 2, 3)
# kwargs: {'status': 'active', 'role': 'admin'}


def introduce(name, age):
    print(f"I am {name} and I am {age} years old.")


# Unpacking a list/tuple using *
my_list = ["Bob", 25]
introduce(*my_list)  # Equivalent to introduce("Bob", 25)

# Unpacking a dictionary using **
my_dict = {"name": "Charlie", "age": 40}
introduce(**my_dict)  # Equivalent to introduce(name="Charlie", age=40)
