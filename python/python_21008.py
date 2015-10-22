# Get the current subclass of the baseclass
def __str__(self):
        return "[{}]:{}".format(self.__class__.__name__, self.blabla)
