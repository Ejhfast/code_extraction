# What is happening when a python class is instantiated but it does not have any __init__() method defined?
class C(A, B): # initializer from A will be used
class C(B, A): # initializer from B will be used
