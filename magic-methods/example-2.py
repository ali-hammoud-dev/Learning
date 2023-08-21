class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"MyClass(name='{self.name}', age={self.age})"

bob = MyClass("ali hammoud", 25)

# Printing the representation of the object
print(repr(bob))
