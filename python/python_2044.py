# Copy **kwargs to self?
class ValidationRule:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
