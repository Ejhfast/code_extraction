# Changing verbose report format for nosetests
def __str__(self):
    return __name__ + "." + self.__class__.__name__ + "." +  self._testMethodName
