# Python: Iterating through constructor's arguments
class foo:
    def __init__(self, **kwargs):
        vars(self).update(kwargs)
