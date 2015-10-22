# python kwargs: how to use best as a filter for objects?
def filter_nodes(self, **kwargs):
    return [n for n in self.pcode
            if all(getattr(n, k) == v for k, v in kwargs.iteritems())]
