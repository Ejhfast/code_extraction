# setattr with kwargs, pythonic or not?
def __init__(self, **kwargs):
    self.__dict__.update( kwargs )
