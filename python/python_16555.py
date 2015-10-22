# Passing a derived class to a function taking a base class in SWIG Python
class Derived(Base):
    def __init__(self):
        super(Derived, self).__init__()
