# django - model unicode() show foreignkey object attribute
def __unicode__(self):
   return '%s %s' % (self.app_id.app_name, self.environ_name)
