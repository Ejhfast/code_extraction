# Accessing "internal variables" of list
def load(self):
    with open(self.filename, 'rb') as inf:
        self[:] = cPickle.load(inf)
