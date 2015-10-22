# Django GenericForeignKey in the admin
def __unicode__(self):
    return 'Comment %s - to  a %s - %s' % (self.pk, self.content_type, self.content_object.__unicode__(), self.timestamp)
