# Naming funtions
def hello_world():
    print("Hello, world!")


hello_world()

# Parameters and arguments
def sum(num1, num2):
    print(num1 + num2)

sum(2, 3)
sum(1, 7)
sum(100, 3)

# Return keyword
def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2

total = sum(7, 2)
print(total)

# Receiving an unknown number of args
def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Sky", "John", "Sara")


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "Sky", last = "Johnny")
