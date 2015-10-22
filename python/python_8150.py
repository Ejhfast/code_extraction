# How do I convert a python list comprehension to a map/filter function calls?
return map(lambda x: x.doSomething(),
           filter(lambda x: x[0] == "z", getIterator()))
