# Way to call super(MyClass, self).__init__() without MyClass?
class B(A):
    def __init__(self):
        A.__init__(self)
