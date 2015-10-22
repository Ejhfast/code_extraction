# Excluding BlobProperty in GAE model in to_dict
def to_dict(self):
  return dict([(p, unicode(getattr(self, p))) for p,t in self.properties().items() if type(t) is not db.BlobProperty])
