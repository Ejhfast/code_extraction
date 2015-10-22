# Which is a more efficient __hash__ implementation in Python objects? Hashing self.__str__, a tuple of attributes, or a real hash routine?
def __hash__(self):
    return hash((self.attr1, self.attr2, self.attr3))
