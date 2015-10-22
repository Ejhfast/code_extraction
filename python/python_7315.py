# I need an object to do anything
class Three(object):
    def __getattr__(self, name):
        return lambda *args, **kw: 3
