# Why default parameter doesn't work for Python object distinguish
def __init__(self, id, list1=None):
    if list1 is None:
        self.list1 = []
