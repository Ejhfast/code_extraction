# Casting to other class in Python
class B(A):
    def __init__(self, obj):
        self.__dict__.update(obj.__dict__)
