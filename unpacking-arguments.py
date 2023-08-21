def add(*args):
    total = 0
    for x in args:
        total += x
    return total


def multiply(*args):
    total = 1
    for x in args:
        total = total * x
    return total


def apply(*args,operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return add(*args)
    else:
        return "No valid operator"
    
print(apply(1,2,3,4,5,operator="*"))

