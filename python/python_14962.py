# Python 2.7 Method Resolution Order overrride
class C(B,A):
    def __init__(self, **kwargs):
        A.__init__(self, **kwargs)
