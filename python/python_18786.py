# How can the name of a class be set automatically in a data attribute of an instance of that class in Python?
self.naturalLanguageString = naturalLanguageString or self.__class__.__name__
