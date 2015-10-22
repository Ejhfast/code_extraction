# How to get rid of _BaseValue
entity = Model(**kwargs)
for name in entity._properties:
    val = getattr(enitity, name)
