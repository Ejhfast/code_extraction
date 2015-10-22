# why python associative map member variable is shared between objects
class A(object):
    def __init__(self):
        self.aMap = {}
