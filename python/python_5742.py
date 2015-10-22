# How to implement followers/following in Django
follows = models.ManyToManyField('self', related_name='follows', symmetrical=False)
