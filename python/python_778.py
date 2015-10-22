# How to list all class properties
property_names=[p for p in dir(SomeClass) if isinstance(getattr(SomeClass,p),property)]
