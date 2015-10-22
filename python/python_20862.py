# How does a super method work in python in case of multiple inheritance?
class B(A):
    def test(self):
        return 'B-&gt;'+super(C, self).test()
