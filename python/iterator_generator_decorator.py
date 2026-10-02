#  Decorator for iterators and generators

def my_logging_decorator(func):
    print(f"Calling function: ")
    func()
    print(f"Finished calling function: ")


@my_logging_decorator
def say_hello():
    print("Hello!")


say_hello()
