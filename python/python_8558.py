# how to refer to a parent method in python?
class B(A):
    def f(self,num):
        return 7 * A.f(self,num)
