# Django models.py Circular Foreign Key
class Album(models.model):
  thumb = models.ForeignKey('Image', null=True, blank=True)
