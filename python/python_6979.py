# Define Self as multiple attributes in Django
def __unicode__(self):
    return u"{0} ({1}, {2})".format(self.icon, self.attrib1, self.attrib2)
