# def named(**kwargs):
#     print(kwargs)
    
# named(name="Bob",age=25)

def named(**kwargs):
    print(kwargs)
    
details = {"name":"ali","age":25}
# named(**details)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg,value in kwargs.items():
        print(f"{arg}")
        print(f"{arg}:{value}")
        
# print_nicely(name="ali",age=25)

def both(*x, **y):
    print(x)
    print(y)
    
# both("ali","hsen",1,name="ali",title = "title")

def example_function(*args, **kwargs):
    print("Positional Arguments (tuple):", args)
    print("Keyword Arguments (dictionary):", kwargs)

example_function(1, 2, 3, name="Alice", age=25)