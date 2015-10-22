# Is it possible in Python to create a class which duplicates the functionality of some class, but changes it's base class?
PyLibMCTagsCache = type("PyLibMCTagsCache",
                        (BaseTagsMemcachedCache,),
                        vars(PyLibMCCache))
