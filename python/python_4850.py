# How do I increment an attribute at runtime using getattr/setattr?
def increment(self, name):
    """Increments a counter specified by the 'name' argument."""
    self.__dict__[name] += 1
