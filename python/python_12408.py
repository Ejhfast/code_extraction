# Inherited class variable modification in Python
class Child(Parent):
    foobar = Parent.foobar + ['world']
