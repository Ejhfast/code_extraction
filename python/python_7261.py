# Can't pickle int object error when object comes from SQLAlchemy?
def __reduce__(self):
    'Return state information for pickling'
    return self.__class__, (int(self.hash_code), str(self.file_pointer))
