# Django: Can I create a QueryDict from a dictionary?
dict = {'a': 'one', 'b': 'two', }
qdict = QueryDict('', mutable=True)
qdict.update(dict)
