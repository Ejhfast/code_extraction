# Django-Models: TypeError: coercing to Unicode: need string or buffer, User found
def __unicode__(self):
     return '%s' % (self.user)
