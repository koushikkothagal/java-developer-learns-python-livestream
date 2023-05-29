import random

class MyClass:
    """This is my first Python class"""
    foo = 10

    def __init__(self, init_value):
        self.foo = init_value
    def print(self):
        print(f'From method{random.random()}')


# Play with adding and removing attributes of a class
# x.bar = 100
# del x.foo
# print(x.__dict__)
# x.print()
# del x.print


# Show difference between function objects and method objects
# print(MyClass.print)
# x = MyClass(20)
# print(x.print)


# Show __class__ property pointing to class object
x = MyClass(20)
print(x.__class__)
