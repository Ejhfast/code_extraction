# Python - unexpected behaviour when using a named constructor argument with empty list default value
def __init__(self, alist=None):
     super(ThingyWithAList, self).__init__()
     self.thelist = [] if alist is None else alist
