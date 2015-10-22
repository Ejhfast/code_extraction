# Attempting to set a stringproperty to default of a md5 of another part of model
@DerivedProperty
def etag(self):
  return hashlib.md5(self.img).hexdigest()
