class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of({self})")
        
    @classmethod
    def class_method(cls):
        print(f"called class_method of {cls}")
        
    @staticmethod
    def static_method():
     print("Called Static_method")
        
test = ClassTest()
# test.instance_method()
# ClassTest.instance_method(test)


## this means ClassTest.class_method(ClassTest)
## without initialization
ClassTest.static_method() 