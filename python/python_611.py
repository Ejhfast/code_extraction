# adding a **kwarg to a class
if kwargs.has_key('bases_queryset'):
    bases_queryset = kwargs['bases_queryset']
    del kwargs['bases_queryset']
