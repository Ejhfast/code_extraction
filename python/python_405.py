# pythonic way to compare compound classes?
class CItem(list):
    def __eq__(self, other):
        return list.__eq__(self, other) and self.__dict__ == other.__dict__
