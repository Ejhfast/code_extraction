# Define a property using methods from the parent class
class Child(MyClass):
    name = property(MyClass.get_name, MyClass.set_name)
