# Django using add to add a ManyToManyField where the object is 'self'
following = models.ManyToManyField('self', symmetrical=False)
