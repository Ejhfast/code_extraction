# Is there a way to "one-line" this using list/set comprehension?
subclasses = set(cls.__subclasses__())
return subclasses + set(sc.get_subclasses() for sc in subclasses)
